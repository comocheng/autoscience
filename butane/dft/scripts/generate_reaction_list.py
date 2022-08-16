# Script to generate the CSV containing the list of reactions in RMG order
# TODO add Cantera order to this list

import pandas as pd
import rmgpy.chemkin


def species_sort(sp1):
    return sp1.molecule[0].smiles


# Copied from AutoTST: reaction.get_label()
def reaction2SMILES(reaction):
    string = ""
    for react in reaction.reactants:
        if isinstance(react, rmgpy.species.Species):
            string += f"{react.molecule[0].to_smiles()}+"
        elif isinstance(react, rmgpy.molecule.Molecule):
            string += f"{react.to_smiles()}+"
    string = string[:-1]
    string += "_"
    for prod in reaction.products:
        if isinstance(prod, rmgpy.species.Species):
            string += f"{prod.molecule[0].to_smiles()}+"
        elif isinstance(prod, rmgpy.molecule.Molecule):
            string += f"{prod.to_smiles()}+"
    label = string[:-1]
    return label


chemkin_path = "/work/westgroup/harris.se/autoscience/autoscience/butane/rmg_model/chem_annotated.inp"
dictionary_path = "/work/westgroup/harris.se/autoscience/autoscience/butane/rmg_model/species_dictionary.txt"
transport_path = "/work/westgroup/harris.se/autoscience/autoscience/butane/rmg_model/tran.dat"
species_list, reaction_list = rmgpy.chemkin.load_chemkin_file(
    chemkin_path,
    dictionary_path=dictionary_path,
    transport_path=transport_path
)


entries = []
for i, reaction in enumerate(reaction_list):
    reaction.products.sort(key=species_sort)
    reaction.reactants.sort(key=species_sort)
    entries.append([i, str(reaction), reaction2SMILES(reaction)])

df = pd.DataFrame(entries, columns=['i', 'name', 'SMILES'])
csv_path = "/work/westgroup/harris.se/autoscience/autoscience/butane/dft/reaction_list.csv"
df.to_csv(csv_path)
