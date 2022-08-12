# Script to generate uncorrelated models for a mechanism
# note, avoids deepcopy due to some issues copying rmgpy data types

import os
import sys
import pickle
import subprocess

import numpy as np
import rmgpy.chemkin

import matplotlib.pyplot as plt


def perturb_reaction(rxn, delta):
    # takes in an RMG reaction object
    # delta is the ln(k) amount to perturb the A factor
    # delta is a multiplicative factor- units don't matter, yay!
    # does not deepycopy because there's some issues with rmgpy.reactions copying
    rxn.kinetics.A.value *= np.exp(delta)


# hooks for parallelizing
models_per_script = 100  # 100 is good
model_num = int(sys.argv[1])

n_ign_delays = 5000
np.random.seed(400)
n_to_perturb = 30

# Load the model
basedir = '/work/westgroup/harris.se/autoscience/autoscience/butane'
model_dir = '/scratch/harris.se/autoscience/uncorrelated/models'  # where the output cti's go

base_chemkin = os.path.join(basedir, 'chem_annotated.inp')
dictionary = os.path.join(basedir, 'species_dictionary.txt')
transport = os.path.join(basedir, 'tran.dat')
species_list, reaction_list = rmgpy.chemkin.load_chemkin_file(base_chemkin, dictionary_path=dictionary, transport_path=transport)

# Load the covariance matrix
covariance_file = '/work/westgroup/harris.se/autoscience/autoscience/uncertainty/butane_covariance.pickle'
with open(covariance_file, 'rb') as handle:
    Sigma_k = pickle.load(handle)


# create a random order of the reactions from which to select the ones to perturb
orders = np.zeros((n_ign_delays, len(reaction_list)))
for i in range(0, n_ign_delays):
    orders[i, :] = np.random.permutation(len(reaction_list))
orders = orders.astype(int)


# Generate the models
for k in range(model_num * models_per_script, (model_num + 1) * models_per_script):
    reactions_to_perturb = orders[k, :]

    # load a fresh model because we can't use deepcopy
    species_list, reaction_list = rmgpy.chemkin.load_chemkin_file(base_chemkin, dictionary_path=dictionary, transport_path=transport)

    np.random.seed(400)

    perturbed_reactions = 0
    for i in range(0, len(reaction_list)):
        reaction_index = orders[k, i]

        if type(reaction_list[reaction_index].kinetics) == rmgpy.kinetics.arrhenius.MultiArrhenius:
            continue
        if type(reaction_list[reaction_index].kinetics) == rmgpy.kinetics.falloff.ThirdBody:
            continue
        if type(reaction_list[reaction_index].kinetics) == rmgpy.kinetics.falloff.Troe:
            continue
        if type(reaction_list[reaction_index].kinetics) == rmgpy.kinetics.arrhenius.PDepArrhenius:
            continue
        if type(reaction_list[reaction_index].kinetics) == rmgpy.kinetics.arrhenius.MultiPDepArrhenius:
            continue
        if type(reaction_list[reaction_index].kinetics) == rmgpy.kinetics.falloff.Lindemann:
            continue
        if type(reaction_list[reaction_index].kinetics) == rmgpy.kinetics.chebyshev.Chebyshev:
            continue

        a = 1.0 / (4.0 * np.sqrt(3.0 * Sigma_k[reaction_index, reaction_index]))
        delta = np.random.uniform(low=-a, high=a)
        perturb_reaction(reaction_list[reaction_index], delta)

        if perturbed_reactions > n_to_perturb:
            break

        perturbed_reactions += 1

    # save the new mechanism
    chemkin_file = os.path.join(model_dir, f'chem_{k:04}.inp')
    rmgpy.chemkin.save_chemkin_file(chemkin_file, species_list, reaction_list, verbose=True, check_for_duplicates=True)
    subprocess.run(['ck2cti', f'--input={chemkin_file}', f'--transport={transport}', f'--output={model_dir}/chem_{k:04}.cti'])
    os.remove(chemkin_file)
