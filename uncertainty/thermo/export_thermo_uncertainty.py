import numpy as np
import rmgpy.tools.uncertainty
import pickle
import json
import matplotlib.pyplot as plt


# load the model
# chemkin = '../../butane/models/rmg_model/chem_annotated.inp'
# species_dict = '../../butane/models/rmg_model/species_dictionary.txt'
chemkin = '/home/moon/autoscience/autoscience/butane/models/rmg_model/chem_annotated.inp'
species_dict = '/home/moon/autoscience/autoscience/butane/models/rmg_model/species_dictionary.txt'

uncertainty = rmgpy.tools.uncertainty.Uncertainty(output_directory='rmg_uncertainty')
uncertainty.load_model(chemkin, species_dict)


# TODO - force the user to provide the input file used to generate the mechanism to ensure databases are really the same
# load the database
# --------------- CAUTION!!! Databases here must match the ones used to generate the mechanism
# note - this cell stalls out on Discovery
thermo_libs = [
    'BurkeH2O2',
    'primaryThermoLibrary',
    'FFCM1(-)',
    'CurranPentane',
    'Klippenstein_Glarborg2016',
    'thermo_DFT_CCSDTF12_BAC',
    'DFT_QCI_thermo',
    'CBS_QB3_1dHR',
]

kinetic_libs = [
    'FFCM1(-)',
    'CurranPentane',
    'combustion_core/version5',
    'Klippenstein_Glarborg2016',
    'BurkeH2O2inArHe',
    'BurkeH2O2inN2',
]
uncertainty.load_database(
    thermo_libraries=thermo_libs,
    kinetics_families='default',
    reaction_libraries=kinetic_libs,
    kinetics_depositories=['training'],
)


# Get the different kinetic and thermo sources
uncertainty.extract_sources_from_model()
uncertainty.assign_parameter_uncertainties()

print()
# with open('correlation_matrix.pickle', 'wb') as handle:
#     pickle.dump(Sigma_k, handle, protocol=pickle.HIGHEST_PROTOCOL)

