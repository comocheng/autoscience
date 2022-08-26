# notebook to run sensitivity on an RMG mechanism
# outputs a CSV of the results
# RMG reaction #, delay

import os
import concurrent.futures

import pandas as pd
import numpy as np
import rmgpy.chemkin
import cantera as ct


# inputs to this script:
condition_index = 7

# Load the base model
# basedir = '/work/westgroup/harris.se/autoscience/autoscience/butane/rmg_model'
basedir = '/work/westgroup/harris.se/autoscience/autoscience/butane/naive_rmg_model'
# model_dir = '/scratch/harris.se/autoscience/local_sensitivity/models'
model_dir = '/scratch/harris.se/autoscience/naive_model/sensitivity/models'  # where all the perturbed models can be found

base_chemkin = os.path.join(basedir, 'chem_annotated.inp')
dictionary = os.path.join(basedir, 'species_dictionary.txt')
transport = os.path.join(basedir, 'tran.dat')
species_list, reaction_list = rmgpy.chemkin.load_chemkin_file(base_chemkin, dictionary_path=dictionary, transport_path=transport)


# Initialize results array
results_dir = os.path.join(os.path.dirname(model_dir), 'results')
os.makedirs(results_dir, exist_ok=True)
csv_path = os.path.join(results_dir, f'ignition_delays_{condition_index:04}.csv')

n_models = len(species_list) + len(reaction_list)
delay_times = np.zeros(n_models)


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


# Take Reactor Conditions from Table 7 of supplementary info in
# https://doi-org.ezproxy.neu.edu/10.1016/j.combustflame.2010.01.016
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


def process_model(model_number):

    model_path = os.path.join(model_dir, f'chem_{model_number:04}.cti')
    if not os.path.exists(model_path):
        return -1

    rmg_gas = ct.Solution(model_path)

    # run the simulations
    X = concentrations[condition_index]
    delay_time = get_delay(rmg_gas, T7[condition_index], P7[condition_index], X)

    return delay_time


for i in range(0, 20):

    model_numbers = np.arange(100 * i, min(100 * (i + 1), len(delay_times)))
    # model_numbers = np.arange(0, n_models)
    with concurrent.futures.ProcessPoolExecutor(max_workers=24) as executor:
        for model_number, delay_time in zip(model_numbers, executor.map(process_model, model_numbers)):
            delay_times[model_number] = delay_time
    # save every 100
    delay_df = pd.DataFrame(delay_times)
    delay_df.to_csv(csv_path)
