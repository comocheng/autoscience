# script to copy over completed results from nheptane dft calculations
import os
import numpy as np
import pandas as pd
import shutil

heptane_sp_list_path = '/work/westgroup/harris.se/autoscience/autoscience_workflow/resources/species_list.csv'
butane_sp_list_path = '/work/westgroup/harris.se/autoscience/autoscience/butane/dft/species_list.csv'

heptane_thermo_dir = '/work/westgroup/harris.se/autoscience/autoscience_workflow/results/dft/thermo'
butane_thermo_dir = '/work/westgroup/harris.se/autoscience/autoscience/butane/dft/thermo'


heptane_species_df = pd.read_csv(heptane_sp_list_path)
butane_species_df = pd.read_csv(butane_sp_list_path)


for i in range(0, len(butane_species_df)):
    butane_index = butane_species_df['i'].values[i]
    smiles = butane_species_df['SMILES'].values[i]
    heptane_index = ''
    if smiles in heptane_species_df['SMILES'].values:
        j = np.where(heptane_species_df['SMILES'].values == smiles)[0]
        heptane_index = heptane_species_df['i'].values[j][0]

        # print(butane_species_df['i'].values[i], smiles, '\t\t', heptane_index)

        heptane_sp_dir = os.path.join(heptane_thermo_dir, f'species_{heptane_index:04}')
        butane_sp_dir = os.path.join(butane_thermo_dir, f'species_{butane_index:04}')
        if os.path.exists(heptane_sp_dir):
            # os.makedirs(butane_sp_dir, exist_ok=True)
            print(f"Copying {heptane_index} {smiles} from heptane to {butane_index} butane")
            # print(f"Copying {heptane_sp_dir} to {butane_sp_dir}")
            try:
                shutil.copytree(heptane_sp_dir, butane_sp_dir)
            except FileExistsError:
                continue
