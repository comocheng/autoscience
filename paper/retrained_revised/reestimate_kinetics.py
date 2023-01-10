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


include_resonance_structures = False


def is_isomorphic_to_resonance_structures(mol1, mol2):
    """
    Checks if the two molecules are isomorphic to each other
    or to any of the resonance structures of the other molecule.
    """
    if mol1.is_isomorphic(mol2):
        return True
    for mol in mol2.generate_resonance_structures():
        if mol1.is_isomorphic(mol):
            return True
    return False


def check_isomorphic(mol1, mol2):
    """
    Checks if the two molecules are isomorphic to each other
    or to any of the resonance structures of the other molecule.
    """
    if include_resonance_structures:
        return is_isomorphic_to_resonance_structures(mol1, mol2)
    else:
        return mol1.is_isomorphic(mol2)


def relabel2_2(input_r, family):
    input_reaction = copy.deepcopy(input_r)

    # copied from AutoTST.autotst.reaction.py
    def get_rmg_mol(smile):
        smiles_conversions = {
            "[CH]": "[CH...]",
            "CARBONMONOXIDE": "[C-]#[O+]"
        }

        if smile.upper() in list(smiles_conversions.keys()):
            smile = smiles_conversions[smile.upper()]
        return rmgpy.molecule.Molecule(smiles=smile).generate_resonance_structures()

    rmg_reactants = [get_rmg_mol(sp.smiles) for sp in input_reaction.reactants]
    rmg_products = [get_rmg_mol(sp.smiles) for sp in input_reaction.products]

    combos_to_try = list(itertools.product(
        list(itertools.product(*rmg_reactants)),
        list(itertools.product(*rmg_products))
    ))

    for rmg_reactants, rmg_products in combos_to_try:
        test_reaction_fwd = rmgpy.reaction.Reaction(
            reactants=list(rmg_reactants),
            products=list(rmg_products)
        )
        test_reaction_rev = rmgpy.reaction.Reaction(
            reactants=list(rmg_products),
            products=list(rmg_reactants)
        )

        for test_reaction in [test_reaction_fwd, test_reaction_rev]:

            try:
                labeled_r, labeled_p = ref_db.kinetics.families[family].get_labeled_reactants_and_products(
                    test_reaction.reactants,
                    test_reaction.products
                )

                if labeled_r is None or labeled_p is None:
                    continue

                if check_isomorphic(input_reaction.reactants[0].molecule[0], labeled_r[0]) and \
                        check_isomorphic(input_reaction.reactants[1].molecule[0], labeled_r[1]):
                    input_reaction.reactants[0].molecule[0] = labeled_r[0]
                    input_reaction.reactants[1].molecule[0] = labeled_r[1]
                elif check_isomorphic(input_reaction.reactants[0].molecule[0], labeled_r[1]) and \
                        check_isomorphic(input_reaction.reactants[1].molecule[0], labeled_r[0]):
                    input_reaction.reactants[0].molecule[0] = labeled_r[1]
                    input_reaction.reactants[1].molecule[0] = labeled_r[0]
                else:
                    continue

                if check_isomorphic(input_reaction.products[0].molecule[0], labeled_p[0]) and \
                        check_isomorphic(input_reaction.products[1].molecule[0], labeled_p[1]):
                    input_reaction.products[0].molecule[0] = labeled_p[0]
                    input_reaction.products[1].molecule[0] = labeled_p[1]
                elif check_isomorphic(input_reaction.products[0].molecule[0], labeled_p[1]) and \
                        check_isomorphic(input_reaction.products[1].molecule[0], labeled_p[0]):
                    input_reaction.products[0].molecule[0] = labeled_p[1]
                    input_reaction.products[1].molecule[0] = labeled_p[0]
                else:
                    continue

                return input_reaction

            except ActionError:
                pass
    return False


def get_new_kinetics(reaction):

    ref_db.kinetics.families[family].add_atom_labels_for_reaction(reaction)
    # test_reaction = relabel2_2(reaction, family)
    # if not test_reaction:
    #     print(f'failed for reaction {reaction}')
    #     return reaction.kinetics

    try:
        template = ref_db.kinetics.families[family].get_reaction_template(reaction)
        # checklabels:

        # template = ref_db.kinetics.families[family].get_reaction_template(reaction)
        # return ref_db.kinetics.families[family].get_kinetics_for_template(template)[0].to_arrhenius(1000)

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
