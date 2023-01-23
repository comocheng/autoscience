# Script to plot all ignition delays

import os
import cantera as ct
import numpy as np
import pandas as pd
import concurrent.futures


import matplotlib.pyplot as plt


def get_delay(gas, T, P, X):
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

    slopes = np.gradient(P, times)
    i = np.argmax(slopes)
    return times[i]


# Load the models
this_dir = os.path.dirname(__file__)
base_rmg_path = os.path.join(this_dir, '../../butane/models/rmg_model/chem_annotated.cti')  # base RMG
# aramco_path = '../models/aramco.cti'
improved_rmg_path = os.path.join(this_dir, '../../butane/models/rmg_model/cutoff3_20230113.cti')

# base_rmg_gas = ct.Solution(base_rmg_path)
# # aramco_gas = ct.Solution(aramco_path)
# improved_model_gas = ct.Solution(improved_model_path)

tables_to_plot = [i for i in range(1, 13)]


# Load the experimental conditions

ignition_delay_data = os.path.join(this_dir, '../../butane/experimental_data/butane_ignition_delay.csv')
df_exp = pd.read_csv(ignition_delay_data)
for table_index in tables_to_plot:

    # slice just table in question
    one_table = df_exp[df_exp['Table'] == table_index]
    # Define Initial conditions using experimental data
    tau = one_table['time (ms)'].values.astype(float)  # ignition delay
    T = one_table['T_C'].values  # Temperatures
    P = one_table['nominal pressure(atm)'].values * ct.one_atm  # pressures in atm

    # list of starting conditions
    # Mixture compositions taken from table 2 of
    # https://doi-org.ezproxy.neu.edu/10.1016/j.combustflame.2010.01.016
    phi = one_table['phi'].values[0]
    if phi == 0.3:
        x_diluent = 0.7821
        conc_dict = {
            'O2(2)': 0.2083,
            'butane(1)': 0.00962
        }
    elif phi == 0.5:
        x_diluent = 0.7771
        conc_dict = {
            'O2(2)': 0.2070,
            'butane(1)': 0.01595
        }
    elif phi == 1.0:
        x_diluent = 0.7649
        conc_dict = {
            'O2(2)': 0.2038,
            'butane(1)': 0.03135
        }
    elif phi == 2.0:
        x_diluent = 0.7416
        conc_dict = {
            'O2(2)': 0.1976,
            'butane(1)': 0.06079
        }

    concentrations = []
    for i in range(0, len(one_table)):
        x_N2 = one_table['%N2'].values[i] / 100.0 * x_diluent
        x_Ar = one_table['%Ar'].values[i] / 100.0 * x_diluent
        x_CO2 = one_table['%CO2'].values[i] / 100.0 * x_diluent
        conc_dict['N2'] = x_N2
        conc_dict['Ar'] = x_Ar
        conc_dict['CO2(7)'] = x_CO2
        concentrations.append(conc_dict)

    def run_simulation(cti_path, condition_index):
        gas = ct.Solution(cti_path)
        X = concentrations[condition_index]
        delay = get_delay(gas, T[condition_index], P[condition_index], X)
        print(f'Completed {condition_index}:\t {delay}')
        return delay

    # Run all simulations in parallel for Base RMG model:
    base_rmg_delays = np.zeros(len(one_table))
    condition_indices = np.arange(0, len(one_table))
    with concurrent.futures.ProcessPoolExecutor(max_workers=16) as executor:
        for condition_index, delay_time in zip(condition_indices, executor.map(run_simulation, [base_rmg_path for x in condition_indices], condition_indices)):
            base_rmg_delays[condition_index] = delay_time

    improved_rmg_delays = np.zeros(len(one_table))
    with concurrent.futures.ProcessPoolExecutor(max_workers=16) as executor:
        for condition_index, delay_time in zip(condition_indices, executor.map(run_simulation, [improved_rmg_path for x in condition_indices], condition_indices)):
            improved_rmg_delays[condition_index] = delay_time

    # plot the ignition delay
    plt.clf()
    plt.plot(1000.0 / T, improved_rmg_delays, marker='x')
    plt.plot(1000.0 / T, base_rmg_delays, marker='x', linestyle='dashed')
    # plt.plot(1000.0 / T, aramco7, marker='x')
    plt.scatter(1000.0 / T, tau / 1000.0, color='black')
    ax = plt.gca()
    ax.set_yscale('log')
    plt.legend(['Improved Model', 'Base RMG', 'Experiment'])
    plt.title('Ignition Delays $\phi$=' + f'{phi}, P={P}')
    plt.xlabel('1000K / T')
    plt.ylabel('Delay (s)')
    plt.savefig(os.path.join(this_dir, f'table_{table_index}.png'))


# # Aramco naming:
# x_diluent = 0.7649
# conc_dict = {
#     'O2': 0.2038,
#     'C4H10': 0.03135
# }

# for i in range(0, len(table7)):
#     x_N2 = table7['%N2'].values[i] / 100.0 * x_diluent
#     x_Ar = table7['%Ar'].values[i] / 100.0 * x_diluent
#     x_CO2 = table7['%CO2'].values[i] / 100.0 * x_diluent
#     conc_dict['N2'] = x_N2
#     conc_dict['AR'] = x_Ar
#     conc_dict['CO2'] = x_CO2
#     concentrations.append(conc_dict)
