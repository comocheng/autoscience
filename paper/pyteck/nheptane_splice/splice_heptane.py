# script to splice in better reactions into the heptane mechanism
import os
import subprocess
import numpy as np

import rmgpy.chemkin
import rmgpy.data.kinetics

# Load the base model
basedir = '/home/moon/autoscience/autoscience/paper/pyteck/nheptane_splice/base_model'
new_model_dir = '/home/moon/autoscience/autoscience/paper/pyteck/nheptane_splice/'
base_chemkin = os.path.join(basedir, 'chem_annotated.inp')
dictionary = os.path.join(basedir, 'species_dictionary.txt')
transport = os.path.join(basedir, 'tran.dat')
species_list, reaction_list = rmgpy.chemkin.load_chemkin_file(base_chemkin, dictionary_path=dictionary, transport_path=transport)
print(f'{len(species_list)} species, {len(reaction_list)} reactions')

# Load the new kinetics library
DFT_DIR = "/home/moon/autoscience/autoscience/butane/dft/"
kinetics_lib = os.path.join(DFT_DIR, 'kinetics', 'kinetics')
ark_kinetics_database = rmgpy.data.kinetics.KineticsDatabase()
ark_kinetics_database.load_libraries(kinetics_lib)
print(f'{len(ark_kinetics_database.libraries[""].entries)} kinetics entries loaded')
