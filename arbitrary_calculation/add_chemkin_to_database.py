# script to add a chemkin file to the species_list.csv and reaction_list.csv
# in the Autoscience repo

import os
import sys
import pandas as pd
import rmgpy.chemkin

sys.path.append('/home/moon/autoscience/autoscience_workflow/workflow/scripts/kinetics')
import kineticfun
# from kineticfun import smiles2reaction


# Read in the mechanism
if len(sys.argv) == 1:
    chemkin_file = '/home/moon/autoscience/autoscience/paper/models/pentane/chem_annotated_fixed.inp'
else:
    chemkin_file = sys.argv[1]

species_dict = os.path.join(os.path.dirname(chemkin_file), 'species_dictionary.txt')
transport = os.path.join(os.path.dirname(chemkin_file), 'tran.dat')
species_list, reaction_list = rmgpy.chemkin.load_chemkin_file(chemkin_file, species_dict)

isomorphic_dict = {}


this_dir = os.path.dirname(os.path.abspath(__file__))
DFT_DIR = os.path.join(this_dir, '..', 'butane', 'dft')


def add_species_list(species_list):
    # Add the species to the species_list.csv
    species_csv = os.path.join(DFT_DIR, 'species_list.csv')
    species_df = pd.read_csv(species_csv)

    if 'Unnamed: 0' in species_df.keys():  
        species_df = species_df.drop(columns=['Unnamed: 0'])

    # for each item on the species list, check if it's already in the database
    smiles_to_add = set()
    species_to_add = []
    for species in species_list:
        species_smiles = species.smiles
        if species_smiles not in species_df.SMILES.values and species_smiles not in smiles_to_add:
            # only add if the smiles is not already in the database
            species_to_add.append(species)
            smiles_to_add.add(species_smiles)

    # add all the new species:
    starting_length = len(species_df)
    for i in range(0, len(species_to_add)):
        new_entry = {
            'i': starting_length + i,
            'name': str(species_to_add[i]),
            'SMILES': species_to_add[i].smiles
        }
        print(f'adding new entry {new_entry}')
        species_df = species_df.append(new_entry, ignore_index=True)

    # save the new results
    species_df.to_csv(species_csv)


def sort_reaction_smiles(reaction_smiles):
    # sort the reactants and products in the reaction smiles

    # handle charged species

    reaction_smiles = reaction_smiles.replace('[C-]#[O+]', 'carbonmonoxide')
    reaction_smiles = reaction_smiles.replace('[O-][N+]#C', 'formonitrileoxide')
    reaction_smiles = reaction_smiles.replace('[O-][N+]=C', 'methylenenitroxide')

    reactants, products = reaction_smiles.split('_')
    reactants = reactants.split('+')
    products = products.split('+')
    reactants.sort()
    products.sort()
    reactants = '+'.join(reactants)
    products = '+'.join(products)
    reaction_smiles = reactants + '_' + products

    reaction_smiles = reaction_smiles.replace('carbonmonoxide', '[C-]#[O+]')
    reaction_smiles = reaction_smiles.replace('formonitrileoxide', '[O-][N+]#C')
    reaction_smiles = reaction_smiles.replace('methylenenitroxide', '[O-][N+]=C')

    return reaction_smiles


def add_reaction_list(reaction_list):
    # Read the reaction csv
    reaction_csv = os.path.join(DFT_DIR, 'reaction_list.csv')
    reaction_df = pd.read_csv(reaction_csv)

    if 'Unnamed: 0' in reaction_df.keys():
        reaction_df = reaction_df.drop(columns=['Unnamed: 0'])

    reactions_to_add = []
    pending_smiles = set()
    # for each reaction, check if it's already in the database
    for j, reaction in enumerate(reaction_list):
        print('trying reaction', j, 'of', len(reaction_list))
        reaction_smiles = sort_reaction_smiles(kineticfun.reaction2smiles(reaction))
        if reaction_smiles in reaction_df.SMILES.values:
            continue

        if reaction_smiles in pending_smiles:
            continue

        pending_smiles.add(reaction_smiles)
        reactions_to_add.append(j)

    # reaction has not been counted yet, so add it
    starting_length = len(reaction_df)
    for i in range(0, len(reactions_to_add)):
        reaction_index = reactions_to_add[i]
        reaction_smiles = kineticfun.reaction2smiles(reaction_list[reaction_index])
        new_entry = {
            'i': starting_length + i,
            'name': str(reaction_list[reaction_index]),
            'SMILES': reaction_smiles
        }
        print(f'adding new entry {new_entry}')
        reaction_df = reaction_df.append(new_entry, ignore_index=True)

    # save the new results
    reaction_df.to_csv(reaction_csv)


if __name__ == '__main__':

    add_species_list(species_list)
    add_reaction_list(reaction_list)
