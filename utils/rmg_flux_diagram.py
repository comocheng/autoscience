# an example of how to generate flux diagrams in RMG
from rmgpy.tools import fluxdiagram

spec_dict = "data/ethane/species_dictionary.txt"
chemkin = "data/ethane/chem.inp"
input_file = "data/ethane/input.py"
output_path = "data/ethane/"
fluxdiagram.create_flux_diagram(input_file, chemkin, spec_dict, save_path=output_path)

