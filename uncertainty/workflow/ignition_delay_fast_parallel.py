# Script to run ignition delay on a model
import os
import concurrent.futures

import numpy as np
import pandas as pd

import cantera as ct


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


# result_dir = '/scratch/harris.se/autoscience/uncorrelated/ignition_delays'
# model_dir = '/scratch/harris.se/autoscience/uncorrelated/models'
result_dir = '/scratch/harris.se/autoscience/not_correlated/ignition_delays'
model_dir = '/scratch/harris.se/autoscience/not_correlated/models'
n_ign_delays = 5000
delay_times = np.zeros(n_ign_delays)


# Load the experimental conditions
ignition_delay_data = '/work/westgroup/harris.se/autoscience/autoscience/butane/butane_ignition_delay.csv'
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


def process_model(model_number):

    model_path = os.path.join(model_dir, f'chem_{model_number:04}.yaml')
    rmg_gas = ct.Solution(model_path)

    # run the simulations
    X = concentrations[i]
    t, T, P, X = run_simulation(rmg_gas, T7[i], P7[i], X)

    index, delay_time = get_ignition_delay(t, T, P, X)
    return delay_time


# for i in range(0, len(table7)):
for i in [7]:  # just do one initial condition

    # for model_number in range(0, n_ign_delays):
    model_numbers = np.arange(0, 100)
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        for model_number, delay_time in zip(model_numbers, executor.map(process_model, model_numbers)):
            delay_times[model_number] = delay_time

    csv_path = os.path.join(result_dir, f'ignition_delays_{i:03}.csv')
    delay_df = pd.DataFrame(delay_times)
    delay_df.to_csv(csv_path)
