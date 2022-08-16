# Script to generate the CSV containing the list of species in RMG order
# TODO add Cantera order to this list

import pandas as pd
import rmgpy.chemkin


chemkin_path = "/work/westgroup/harris.se/autoscience/autoscience/butane/rmg_model/chem_annotated.inp"
dictionary_path = "/work/westgroup/harris.se/autoscience/autoscience/butane/rmg_model/species_dictionary.txt"
transport_path = "/work/westgroup/harris.se/autoscience/autoscience/butane/rmg_model/tran.dat"
species_list, reaction_list = rmgpy.chemkin.load_chemkin_file(
    chemkin_path,
    dictionary_path=dictionary_path,
    transport_path=transport_path
)

entries = []
for i, species in enumerate(species_list):
    entries.append([i, str(species), species.molecule[0].smiles])

df = pd.DataFrame(entries, columns=['i', 'name', 'SMILES'])
csv_path = "/work/westgroup/harris.se/autoscience/autoscience/butane/dft/species_list.csv"
df.to_csv(csv_path)
