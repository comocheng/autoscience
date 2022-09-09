# script to run many flame speeds

import cantera as ct
import numpy as np
import pandas as pd
import concurrent.futures
import sys


if len(sys.argv) > 1:
    cti_path = sys.argv[1]
else:
    # Load the model
    # cti_path = '/work/westgroup/harris.se/autoscience/autoscience/butane/rmg_model/chem_annotated.cti'
    cti_path = '/work/westgroup/harris.se/autoscience/aramco/AramcoMech3.0.MECH.cti'
    # cti_path = '/work/westgroup/harris.se/autoscience/autoscience/butane/naive_rmg_model/chem_annotated.cti'
    cti_path = '/scratch/harris.se/autoscience/naive_model/changed_models/chem_2022-08-25.cti'
    #cti_path = '/work/westgroup/harris.se/autoscience/autoscience/butane/improved_models/chem_2022-08-28.cti'    
    cti_path = '/work/westgroup/harris.se/autoscience/autoscience/butane/improved_models/chem_2022-08-28.cti'    

gas = ct.Solution(cti_path)



# load the experimental conditions
flame_speed_data = '/work/westgroup/harris.se/autoscience/autoscience/butane/butane_flamespeeds.csv'
df_exp = pd.read_csv(flame_speed_data)

# get just the Park data
data_slice = df_exp[df_exp['Reference'] == 'Park et al. 2016']

# Define Initial conditions using experimental data
speeds = data_slice['SL0 (cm/s)'].values.astype(float)  # ignition delay
temperatures = data_slice['Tu (K)'].values  # Temperatures
pressures = data_slice['Pu (atm)'].values * ct.one_atm  # pressures in atm
equiv_ratios = data_slice['Equivalence Ratio'].values  # equivalence ratio


# list of starting conditions
# Define stoichiometric coefficients
v_fuel = 1.0
v_oxidizer = 13.0 / 2.0
v_N2 = 0.79 * (v_oxidizer / 0.21)  # air is approximately 79% N2 and 21% O2

# calculate actual ratio of fuel to oxidizer
actual_ratio = equiv_ratios * (v_fuel / v_oxidizer)


# start with 1.0 oxidizer, then normalize
x_O2 = 1.0
x_C4H10 = actual_ratio * x_O2
x_N2 = 0.79 * (x_O2 / .21)
total = x_O2 + x_C4H10 + x_N2
x_O2 = x_O2 / total
x_C4H10 = x_C4H10 / total
x_N2 = x_N2 / total

# concentrations = [{'C4H10': x_C4H10[i], 'O2': x_O2[i], 'N2': x_N2[i]} for i in range(0, len(equiv_ratios))]
concentrations = [{'butane(1)': x_C4H10[i], 'O2(2)': x_O2[i], 'N2': x_N2[i]} for i in range(0, len(equiv_ratios))]


# function for running a flame speed
# assumes gas has been properly initialized
def run_flame_speed(condition_index):
    gas = ct.Solution(cti_path)

    gas.TPX = temperatures[condition_index], pressures[condition_index], concentrations[condition_index]

    tol_ss = [1.0e-13, 1.0e-9]  # abs and rel tolerances for steady state problem
    tol_ts = [1.0e-13, 1.0e-9]  # abs and rel tie tolerances for time step function

    width = 0.08
    flame = ct.FreeFlame(gas, width=width)
    flame.flame.set_steady_tolerances(default=tol_ss)   # set tolerances
    flame.flame.set_transient_tolerances(default=tol_ts)
    flame.set_refine_criteria(ratio=5, slope=0.25, curve=0.27)
    flame.max_time_step_count = 900
    loglevel = 1

    print("about to solve")
    flame.solve(loglevel=loglevel, auto=True)
    Su = flame.velocity[0]

    return Su


# Run all simulations in parallel
flame_speeds = np.zeros(len(data_slice))
condition_indices = np.arange(0, len(data_slice))
with concurrent.futures.ProcessPoolExecutor(max_workers=16) as executor:
    for condition_index, flame_speed in zip(condition_indices, executor.map(run_flame_speed, condition_indices)):
        flame_speeds[condition_index] = flame_speed


out_df = pd.DataFrame(flame_speeds)
# out_df.to_csv('aramco_flame_speeds.csv')

# out_df.to_csv('naive_improved_flame_speeds.csv')
# out_df.to_csv('rmg_changed_flame_speeds.csv')
out_df.to_csv(f'{cti_path[:-4]}.csv')
