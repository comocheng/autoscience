# Script to run ignition delay on a model
import os
import sys
import logging  # for threadsafe file-writing


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import cantera as ct


# use the logging module for threadsafe result writing
logpath = '/scratch/harris.se/autoscience/uncorrelated/ignition_delays.log'
logger = logging.getLogger('log')
logger.setLevel(logging.INFO)
handle = logging.FileHandler(logpath)
handle.setFormatter(logging.Formatter())
logger.addHandler(handle)


# Set the model #
model_number = int(sys.argv[1])
model_dir = '/scratch/harris.se/autoscience/uncorrelated/models'
img_dir = '/scratch/harris.se/autoscience/uncorrelated/png'
csv_dir = '/scratch/harris.se/autoscience/uncorrelated/csv'

model_path = os.path.join(model_dir, f'chem_{model_number:04}.cti')
rmg_gas = ct.Solution(model_path)

# Load the experimental conditions
ignition_delay_data = '/work/westgroup/harris.se/autoscience/autoscience/butane/butane_ignition_delay.csv'
df = pd.read_csv(ignition_delay_data)

# slice just table 7, where phi=1.0
table7 = df[df['Table'] == 7]
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
    'O2': 0.2038,
    'C4H10': 0.03135
}
for i in range(0, len(table7)):
    x_N2 = table7['%N2'].values[i] / 100.0 * x_diluent
    x_Ar = table7['%Ar'].values[i] / 100.0 * x_diluent
    x_CO2 = table7['%CO2'].values[i] / 100.0 * x_diluent
    conc_dict['N2'] = x_N2
    conc_dict['AR'] = x_Ar
    conc_dict['CO2'] = x_CO2
    concentrations.append(conc_dict)


# Take Reactor Conditions from Table 7 of supplementary info in
# https://doi-org.ezproxy.neu.edu/10.1016/j.combustflame.2010.01.016
def run_simulation(gas, T, P, X):
    # function to run a RCM simulation

    t_end = 1.0  # time in seconds
    gas.TPX = T, P, X

    env = ct.Reservoir(ct.Solution('air.xml'))
    reactor = ct.IdealGasReactor(gas)
    wall = ct.Wall(reactor, env, A=1.0, velocity=0)
    reactor_net = ct.ReactorNet([reactor])

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

    if plot:
        # plot to check if the answer makes sense
        plt.clf()
        plt.plot(times, P)
        plt.axvline(x=times[i], color='green')
        max_time = min(times[i] * 1.1, times[-1])
        plt.xlim([0, max_time])
        plt.xlabel('Time (s)')
        plt.ylabel('Pressure (Pa)')

        if title:
            plt.title(title)
        else:
            plt.title('Ignition Delay')

        if save:
            plt.savefig(save)

    return i, times[i]
    # look for time when it reaches half of maximum pressure


# create empty arrays for the models
rmg_tau7 = np.zeros(len(tau7))

# run the simulations
# for i in range(0, len(table7)):
conditions_index = [7]  # only do the analysis at one set of conditions
for i in conditions_index:
    X = f'O2(2):{concentrations[i]["O2"]}, butane(1):{concentrations[i]["C4H10"]}, Ar:{concentrations[i]["AR"]},  CO2(7):{concentrations[i]["CO2"]}, N2:{concentrations[i]["N2"]}'
    t, T, P, X = run_simulation(rmg_gas, T7[i], P7[i], X)

    index, delay_time = get_ignition_delay(t, T, P, X)

    # write in the following format:
    # model  conditions_index  ignition delay
    logger.info(f'{model_number:04} {i} {delay_time}')

    # # save the csv
    # data = np.concatenate((np.matrix(t).transpose(), np.matrix(T).transpose(), np.matrix(P).transpose(), X), axis=1)
    # columns = ['t', 'T', 'P'] + rmg_gas.species_names
    # out_df = pd.DataFrame(data=data, columns=columns)
    # csv_name = os.path.join(csv_dir, f'model_{model_number:04}_7-{i:04}.csv')
    # out_df.to_csv(csv_name)

    # save_name = os.path.join(img_dir, f'model_{model_number:04}_7-{i:04}.png')
    # index, delay_time = get_ignition_delay(t, T, P, X, plot=True, save=save_name)
    # rmg_tau7[i] = delay_time
