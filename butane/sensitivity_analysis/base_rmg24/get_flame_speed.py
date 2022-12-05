# script to run single flame speed for mass parallelization
import cantera as ct
import numpy as np
import pandas as pd
import sys

import os
import sys
import copy

import rmgpy.chemkin


model_num = int(sys.argv[1])
model_dir = '/work/westgroup/harris.se/autoscience/autoscience/butane/sensitivity_analysis/base_rmg24/models'
cti_path = os.path.join(model_dir, f'chem_{model_num:04}.cti')


# load the experimental conditions
flame_speed_data = '/work/westgroup/harris.se/autoscience/autoscience/butane/experimental_data/butane_flamespeeds.csv'
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


flame_speed = run_flame_speed(4)  # run at condition 4 - phi=1.0

results_dir = '/work/westgroup/harris.se/autoscience/autoscience/butane/sensitivity_analysis/base_rmg24/results/flame_speeds'
outfile = os.path.join(results_dir, f'flame_speed_{model_num:04}.txt')
with open(outfile, 'w') as f:
    f.write(str(flame_speed))
