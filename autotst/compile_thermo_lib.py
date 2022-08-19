#!/usr/bin/env python
# script to collect all of the thermo calculations and put them together into a database

import os
import re
import glob
import rmgpy.data.thermo
from collections import OrderedDict


DFT_DIR = "/work/westgroup/harris.se/autoscience/autoscience/butane/dft/"
thermo_libs = glob.glob(os.path.join(DFT_DIR, 'thermo', 'species*', 'arkane', 'RMG_libraries'))

# Load the Arkane thermo
entries = []
for i, lib_path in enumerate(thermo_libs):
    matches = re.search('species_([0-9]{4})', lib_path)
    species_index = int(matches[1])
    ark_thermo_database = rmgpy.data.thermo.ThermoDatabase()
    ark_thermo_database.load_libraries(
        lib_path,
    )

    for key in ark_thermo_database.libraries['thermo'].entries.keys():
        entry = ark_thermo_database.libraries['thermo'].entries[key]
        entry.index = species_index
        entries.append(entry)

# compile it all into a single database and a single library which I'll call harris_butane
ark_thermo_database = rmgpy.data.thermo.ThermoDatabase()
ark_thermo_database.libraries['thermo'] = rmgpy.data.thermo.ThermoLibrary()
ark_thermo_database.libraries['thermo'].label = 'harris_butane'
ark_thermo_database.libraries['thermo'].entries = OrderedDict()
for entry in entries:
    ark_thermo_database.libraries['thermo'].entries[entry.label] = entry

# save the results
output_path = os.path.join(DFT_DIR, 'thermo')
ark_thermo_database.save_libraries(output_path)

