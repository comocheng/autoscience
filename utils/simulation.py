import os
import sys
import copy
import numpy as np
import pandas as pd
import futures


import cantera as ct
import rmgpy.chemkin


# Take Reactor Conditions from Table 7 of supplementary info in
# https://doi-org.ezproxy.neu.edu/10.1016/j.combustflame.2010.01.016
def run_simulation(gas, T, P, X):
    # function to run a RCM simulation

    t_end = 1.0  # time in seconds
    gas.TPX = T, P, X

    env = ct.Reservoir(ct.Solution('air.yaml'))
    # env = ct.Reservoir(ct.Solution('air.xml'))
    reactor = ct.IdealGasReactor(gas)
    wall = ct.Wall(reactor, env, A=1.0, velocity=0)
    reactor_net = ct.ReactorNet([reactor])
    # # allegedly faster solving
    # reactor_net.derivative_settings = {"skip-third-bodies": True, "skip-falloff": True}
    # reactor_net.preconditioner = ct.AdaptivePreconditioner()

    times = [0]
    T = [reactor.T]
    P = [reactor.thermo.P]
    X = [reactor.thermo.X]  # mol fractions
    while reactor_net.time < t_end:
        reactor_net.step()

        times.append(reactor_net.time)
        T.append(reactor.T)
        P.append(reactor.thermo.P)
        X.append(reactor.thermo.X)

    return (times, T, P, X)


def get_ignition_delay(times, T, P, X, plot=False, title='', save=''):
    # look for time with largest derivative
    slopes = np.gradient(P, times)
    i = np.argmax(slopes)
    return i, times[i]


# Load the experimental conditions
ignition_delay_data = '/work/westgroup/harris.se/autoscience/autoscience/butane/experimental_data/butane_ignition_delay.csv'
df_exp = pd.read_csv(ignition_delay_data)

# slice just table 7, where phi=1.0
table7 = df_exp[df_exp['Table'] == 7]
# Define Initial conditions using experimental data
tau7 = table7['time (ms)'].values.astype(float)  # ignition delay
T7 = table7['T_C'].values  # Temperatures
P7 = table7['nominal pressure(atm)'].values * ct.one_atm  # pressures in atm
# list of starting conditions
# Mixture compositions taken from table 2 of
# https://doi-org.ezproxy.neu.edu/10.1016/j.combustflame.2010.01.016
concentrations = []
# for phi = 1
x_diluent = 0.7649
conc_dict = {
    'O2(2)': 0.2038,
    'butane(1)': 0.03135
}

for i in range(0, len(table7)):
    x_N2 = table7['%N2'].values[i] / 100.0 * x_diluent
    x_Ar = table7['%Ar'].values[i] / 100.0 * x_diluent
    x_CO2 = table7['%CO2'].values[i] / 100.0 * x_diluent
    conc_dict['N2'] = x_N2
    conc_dict['Ar'] = x_Ar
    conc_dict['CO2(7)'] = x_CO2
    concentrations.append(conc_dict)


def get_delay(cti_path, condition_index=7):
    # load a fresh model
    gas = ct.Solution(cti_path)
    # run the simulations at condition #7
    i = condition_index
    X = concentrations[i]
    t, T, P, X = run_simulation(gas, T7[i], P7[i], X)
    index, delay_time = get_ignition_delay(t, T, P, X)
    return delay_time



def get_flame_speed(cti_path, condition_index=4):
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

    i = condition_index
    # concentrations = [{'C4H10': x_C4H10[i], 'O2': x_O2[i], 'N2': x_N2[i]} for i in range(0, len(equiv_ratios))]
    concentrations = [{'butane(1)': x_C4H10[i], 'O2(2)': x_O2[i], 'N2': x_N2[i]} for i in range(0, len(equiv_ratios))]

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

    print(f'flame speed: {Su}') 
    results_dir = os.path.dirname(cti_file)
    fs_file = os.path.join(results_dir, 'flame_speed_' + cti_file[-8:-4] + '.csv')
    
    with open(fs_file, 'w') as f:
        f.write(str(Su))



