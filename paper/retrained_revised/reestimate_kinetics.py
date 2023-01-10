# script to take an existing mechanism and splice in new Disproportionation kinetics
# Assumes the RMG-database is set to the refitted tree: sevy/autoscience_retrain_revise
# https://github.com/sevyharris/RMG-database/tree/autoscience_retrain_revise

# imports
import os
import copy
import itertools
import subprocess
import rmgpy
import rmgpy.chemkin
import rmgpy.data.kinetics

from rmgpy.exceptions import ActionError
from rmgpy.exceptions import UndeterminableKineticsError


# Read in the mechanism
chemkin_file = '/home/moon/autoscience/autoscience/butane/models/rmg_model/chem_annotated.inp'
species_dictionary = '/home/moon/autoscience/autoscience/butane/models/rmg_model/species_dictionary.txt'
transport = os.path.join(os.path.dirname(chemkin_file), 'tran.dat')
new_model_dir = os.path.dirname(chemkin_file)
species_list, reaction_list = rmgpy.chemkin.load_chemkin_file(chemkin_file, species_dictionary)


# Load the RMG database
family = 'Disproportionation'
ref_library_path = os.path.join(rmgpy.settings['database.directory'], 'kinetics')
rmg_kinetics_database = rmgpy.data.kinetics.KineticsDatabase()
rmg_kinetics_database.load(
    ref_library_path,
    libraries=[],
    families=[family]
)

thermo_libs = [
    'primaryThermoLibrary',
]

thermo_library_path = os.path.join(rmgpy.settings['database.directory'], 'thermo')
thermo_database = rmgpy.data.thermo.ThermoDatabase()
thermo_database.load(
    thermo_library_path,
    libraries=thermo_libs
)
ref_db = rmgpy.data.rmg.RMGDatabase()
ref_db.kinetics = rmg_kinetics_database
ref_db.thermo = thermo_database


def get_new_kinetics(reaction):
    try:
        ref_db.kinetics.families[family].add_atom_labels_for_reaction(reaction)
        template = ref_db.kinetics.families[family].get_reaction_template(reaction)
        kinetics = ref_db.kinetics.families[family].get_kinetics_for_template(template)[0].to_arrhenius(1000)
        return kinetics
    except UndeterminableKineticsError:
        print(f'failed for reaction {reaction}')
        return reaction.kinetics


# recalculate Disproportionation kinetics
for i, reaction in enumerate(reaction_list):
    if hasattr(reaction, 'family') and reaction.family == family:
        reaction_list[i].kinetics = get_new_kinetics(reaction)

# save the new chemkin and cantera
new_chemkin_file = os.path.join(new_model_dir, 'refit_model_20230110.inp')
rmgpy.chemkin.save_chemkin_file(new_chemkin_file, species_list, reaction_list)
subprocess.run(['ck2cti', f'--input={new_chemkin_file}', f'--transport={transport}', f'--output={new_chemkin_file[:-4]}.cti'])
# also save cantera
