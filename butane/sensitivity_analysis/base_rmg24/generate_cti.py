# script to generate cti files for plain sensitivity analysis

import os
import sys
import subprocess

import numpy as np
import rmgpy.chemkin


model_num = int(sys.argv[1])


# Load the base model
model_dir = '/work/westgroup/harris.se/autoscience/autoscience/butane/naive_model/sensitivity/models'  # where the output cti's go

base_chemkin = os.path.join('chem_annotated.inp')
dictionary = os.path.join('species_dictionary.txt')
transport = os.path.join('tran.dat')
species_list, reaction_list = rmgpy.chemkin.load_chemkin_file(base_chemkin, dictionary_path=dictionary, transport_path=transport)


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


def save_new_cti(param_index, reaction=True):
    # if false, we're perturbing a species
    # load a fresh model
    species_list, reaction_list = rmgpy.chemkin.load_chemkin_file(base_chemkin, dictionary_path=dictionary, transport_path=transport)

    if reaction:
        model_index = param_index
        delta = 0.1
        try:
            perturb_reaction(reaction_list[param_index], delta)
        except AttributeError:
            print(f'skipping reaction {param_index} {type(reaction_list[param_index])}')
            return
    else:  # perturb the thermo
        model_index = param_index + len(reaction_list)
        delta = 0.1
        perturb_species(species_list[param_index], delta)

    # save the new mechanism
    chemkin_file = os.path.join(model_dir, f'chem_{model_index:04}.inp')
    cti_file = chemkin_file[:-4] + '.cti'
    rmgpy.chemkin.save_chemkin_file(chemkin_file, species_list, reaction_list, verbose=True, check_for_duplicates=True)
    subprocess.run(['ck2cti', f'--input={chemkin_file}', f'--transport={transport}', f'--output={cti_file}'])
    os.remove(chemkin_file)


if model_num > len(reaction_list):
    save_new_cti(model_num - len(reaction_list), reaction=False)
else:
    save_new_cti(model_num, reaction=True)
