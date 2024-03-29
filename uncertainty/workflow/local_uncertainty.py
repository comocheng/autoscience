# Script to run local sensitivity/uncertainty analysis, 20220815

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


def process_model(reaction_number):
    print(f"Processing Model {reaction_number}")
    gas = ct.Solution(cti_path)
    delta = 1.0
    rxn = gas.reactions()[reaction_number]
    if hasattr(rxn, 'rate') and type(rxn.rate) == ct._cantera.Arrhenius:
        new_reaction = gas.reactions()[reaction_number]
        new_kinetics = ct._cantera.Arrhenius(
            np.exp(delta) * new_reaction.rate.pre_exponential_factor,
            new_reaction.rate.temperature_exponent,
            new_reaction.rate.activation_energy
        )
        new_reaction.rate = new_kinetics
        gas.modify_reaction(reaction_number, new_reaction)

        # run the simulations at condition #7
        i = 7
        X = concentrations[i]
        t, T, P, X = run_simulation(gas, T7[i], P7[i], X)

        index, delay_time = get_ignition_delay(t, T, P, X)
    else:
        delay_time = -1

    return delay_time


# Load the base model
basedir = '/work/westgroup/harris.se/autoscience/autoscience/butane'
cti_path = os.path.join(basedir, 'chem_annotated.cti')
gas = ct.Solution(cti_path)

# define results location
result_dir = '/scratch/harris.se/autoscience/local_sensitivity'
n_ign_delays = len(gas.reactions())
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

# Run the Ignitions
# for i in range(0, len(table7)):
for i in [7]:  # just do one initial condition

    rxn_indices = np.arange(0, n_ign_delays)
    # rxn_indices = np.arange(0, 10)

    with concurrent.futures.ProcessPoolExecutor(max_workers=16) as executor:
        for reaction_index, delay_time in zip(rxn_indices, executor.map(process_model, rxn_indices)):
            delay_times[reaction_index] = delay_time

    csv_path = os.path.join(result_dir, f'ignition_delays_{i:03}.csv')
    delay_df = pd.DataFrame(delay_times)
    delay_df.to_csv(csv_path)
