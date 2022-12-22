# script to splice in better reactions into the heptane mechanism
import os
import subprocess
import numpy as np

import rmgpy.chemkin
import rmgpy.data.kinetics

# Load the base model
basedir = '/work/westgroup/harris.se/autoscience/autoscience/butane/models/rmg_model'


# basedir = '/work/westgroup/harris.se/autoscience/autoscience/debug/s787_rxns/'
new_model_dir = basedir
base_chemkin = os.path.join(basedir, 'chem_annotated.inp')
dictionary = os.path.join(basedir, 'species_dictionary.txt')
transport = os.path.join(basedir, 'tran.dat')
species_list, reaction_list = rmgpy.chemkin.load_chemkin_file(base_chemkin, dictionary_path=dictionary, transport_path=transport)
print(f'{len(species_list)} species, {len(reaction_list)} reactions')
