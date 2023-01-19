# script to add a chemkin file to the species_list.csv and reaction_list.csv
# in the Autoscience repo

import os
import sys
import pandas as pd
import rmgpy.chemkin

sys.path.append('/home/moon/autoscience/autoscience_workflow/workflow/scripts/kinetics')
import kineticfun


this_dir = os.path.dirname(os.path.abspath(__file__))
DFT_DIR = os.path.join(this_dir, '..', 'butane', 'dft')


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


def replace_reaction_list_sorted():
    # Read the reaction csv
    reaction_csv = os.path.join(DFT_DIR, 'reaction_list.csv')
    reaction_df = pd.read_csv(reaction_csv)

    if 'Unnamed: 0' in reaction_df.keys():
        reaction_df = reaction_df.drop(columns=['Unnamed: 0'])

    # for each reaction, check if it's already in the database
    for i in range(0, len(reaction_df)):
        reaction_smiles = reaction_df.SMILES[i]
        new_reaction_smiles = sort_reaction_smiles(reaction_smiles)
        reaction_df.SMILES[i] = new_reaction_smiles
        if reaction_smiles != new_reaction_smiles:
            # check that the reactions are still isomorphic:
            r1 = kineticfun.smiles2reaction(reaction_smiles)
            r2 = kineticfun.smiles2reaction(new_reaction_smiles)
            if not r1.is_isomorphic(r2):
                print('Error: reactions are not isomorphic')
                print(reaction_smiles, '\t', new_reaction_smiles)
                print(r1, '\t', r2)
                exit()

    # save the new results
    reaction_df.to_csv(reaction_csv)


if __name__ == '__main__':
    replace_reaction_list_sorted()
