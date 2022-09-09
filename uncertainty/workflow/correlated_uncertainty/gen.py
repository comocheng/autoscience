import os
import sys
import copy
import pickle
import subprocess

import numpy as np
import rmgpy.chemkin


k = int(sys.argv[1])

# Load the model and the saved uncertainty covariance matrix.
# Only looks at uncorrelated parameters, so you can fill the
# diagonal of a zero matrix and get the same results as using
# the full covariance matrix

basedir = '/work/westgroup/harris.se/autoscience/autoscience/butane/rmg_model'
model_dir = '/scratch/harris.se/autoscience/correlated/models'  # where the output cti's go

base_chemkin = os.path.join(basedir, 'chem_annotated.inp')
dictionary = os.path.join(basedir, 'species_dictionary.txt')
transport = os.path.join(basedir, 'tran.dat')
# RMG_cti_path = os.path.join(basedir, 'chem_annotated.cti')

species_list, reaction_list = rmgpy.chemkin.load_chemkin_file(base_chemkin, dictionary_path=dictionary, transport_path=transport)
# RMG_gas = ct.Solution(RMG_cti_path)


covariance_file = '/work/westgroup/harris.se/autoscience/autoscience/uncertainty/butane_covariance.pickle'
with open(covariance_file, 'rb') as handle:
    Sigma_k = pickle.load(handle)


uniform_randoms = np.load('randoms1001.npy')


def perturb_reaction(rxn, delta):
    # takes in an RMG reaction object
    # delta is the ln(k) amount to perturb the A factor
    # delta is a multiplicative factor- units don't matter, yay!
    # does not deepycopy because there's some issues with rmgpy.reactions copying

    rxn.kinetics.A.value *= np.exp(delta)


species_list, reaction_list = rmgpy.chemkin.load_chemkin_file(base_chemkin, dictionary_path=dictionary, transport_path=transport)

# perturb all of the reactions
for i in range(0, len(reaction_list)):
    try:
        delta = uniform_randoms[k, i]
        perturb_reaction(reaction_list[i], delta)
    except AttributeError:
        continue

# save the new mechanism
chemkin_file = os.path.join(model_dir, f'chem_{k:04}.inp')
rmgpy.chemkin.save_chemkin_file(chemkin_file, species_list, reaction_list, verbose=True, check_for_duplicates=True)
subprocess.run(['ck2cti', f'--input={chemkin_file}', f'--transport={transport}', f'--output={model_dir}/chem_{k:04}.cti'])
os.remove(chemkin_file)
