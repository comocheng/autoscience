import os
import sys
import copy
import subprocess


import numpy as np
import rmgpy.chemkin

# Load the base model
basedir = '/work/westgroup/harris.se/autoscience/autoscience/butane/sensitivity_analysis/base_rmg24/'
model_dir = '.'  # where the output cti's go

base_chemkin = os.path.join(basedir, 'chem_annotated.inp')
dictionary = os.path.join(basedir, 'species_dictionary.txt')
transport = os.path.join(basedir, 'tran.dat')
species_list, reaction_list = rmgpy.chemkin.load_chemkin_file(base_chemkin, dictionary_path=dictionary, transport_path=transport)

model_num = int(sys.argv[1])


def perturb_species(species, delta):
    # takes in an RMG species object
    # change the enthalpy offset
    for poly in species.thermo.polynomials:
        new_coeffs = poly.coeffs
        new_coeffs[5] *= (1.0 + delta)
        poly.coeffs = new_coeffs


def perturb_reaction(rxn, delta):
    # takes in an RMG reaction object
    # delta is the ln(k) amount to perturb the A factor
    # delta is a multiplicative factor- units don't matter, yay!
    # does not deepycopy because there's some issues with rmgpy.reactions copying

    rxn.kinetics.A.value *= np.exp(delta)


def save_new_cti(model_index):
    # load a fresh model
    species_list, reaction_list = rmgpy.chemkin.load_chemkin_file(base_chemkin, dictionary_path=dictionary, transport_path=transport)

    delta = 0.1
    try:
        perturb_reaction(reaction_list[model_index], delta)
    except AttributeError:
        print(f'skipping reaction {model_index} {type(reaction_list[model_index])}')
        return

    # save the new mechanism
    chemkin_file = os.path.join(model_dir, f'chem_{model_index:04}.inp')
    rmgpy.chemkin.save_chemkin_file(chemkin_file, species_list, reaction_list, verbose=True, check_for_duplicates=True)
    subprocess.run(['ck2cti', f'--input={chemkin_file}', f'--transport={transport}', f'--output={model_dir}/chem_{model_index:04}.cti'])
    os.remove(chemkin_file)

save_new_cti(model_num)
