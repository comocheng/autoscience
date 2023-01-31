# This script takes an RMG mechanism and exports the uncertainty
import os
import numpy as np
import rmgpy.tools.uncertainty


# # Load the RMG Model
this_file = os.path.abspath(__file__)
this_dir = os.path.dirname(this_file)
# load the model

chemkin = os.path.join(this_dir, 'chem_annotated_fixed.inp')
species_dict = os.path.join(this_dir, 'species_dictionary.txt')

uncertainty = rmgpy.tools.uncertainty.Uncertainty(output_directory=os.path.join(this_dir, 'rmg_uncertainty'))
uncertainty.load_model(chemkin, species_dict)


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
    kinetics_families=['default'],
    reaction_libraries=kinetic_libs,
    kinetics_depositories=['training'],
)

# Get the different kinetic and thermo sources
uncertainty.extract_sources_from_model()
uncertainty.assign_parameter_uncertainties()


# Create a giant dictionary with all of the reaction family information in it
auto_gen_families = {}
for family_name in uncertainty.database.kinetics.families.keys():
    if family_name == 'Intra_R_Add_Endocyclic' or family_name == 'Intra_R_Add_Exocyclic':
        continue
    if uncertainty.database.kinetics.families[family_name].auto_generated and family_name not in auto_gen_families.keys():
        auto_gen_families[family_name] = uncertainty.database.kinetics.families[family_name].rules.get_entries()
        auto_gen_families[f'{family_name}_labels'] = [entry.label for entry in uncertainty.database.kinetics.families[family_name].rules.get_entries()]
        auto_gen_families[f'{family_name}_rxn_map'] = uncertainty.database.kinetics.families[family_name].get_reaction_matches(
            thermo_database=uncertainty.database.thermo,
            remove_degeneracy=True,
            get_reverse=True,
            exact_matches_only=False,
            fix_labels=True)


sensitivity_dict = {}
for i, rxn in enumerate(uncertainty.reaction_list):
    if 'Rate Rules' in uncertainty.reaction_sources_dict[rxn] and uncertainty.reaction_sources_dict[rxn]['Rate Rules'][1]['node']:
        print(i, uncertainty.reaction_sources_dict[rxn]['Rate Rules'][1]['node_std_dev'])
        sensitivity_dict[i] = uncertainty.reaction_sources_dict[rxn]['Rate Rules'][1]['node_std_dev']
        #         node_name = uncertainty.reaction_sources_dict[rxn]['Rate Rules'][1]['node']


# put the autogenerated tree info into the kinetic sources dictionary
for rxn in uncertainty.reaction_list:
    if hasattr(rxn, 'family'):
        family_name = rxn.family
        if family_name == 'Intra_R_Add_Endocyclic' or family_name == 'Intra_R_Add_Exocyclic':
            continue
    if 'Rate Rules' in uncertainty.reaction_sources_dict[rxn] and uncertainty.reaction_sources_dict[rxn]['Rate Rules'][1]['node']:
        node_name = uncertainty.reaction_sources_dict[rxn]['Rate Rules'][1]['node']
        if 'Earaised' in node_name:
            node_name = node_name.split('Earaised')[0]
        training_reactions = auto_gen_families[f'{rxn.family}_rxn_map'][node_name]

        # TODO use sensitivity instead of equal weight
        w = 1.0 / len(training_reactions)

        uncertainty.reaction_sources_dict[rxn]['Rate Rules'][1]['training'] = [(x, x, w) for x in training_reactions]

# Define Uncertainty Constants
k_nonexact = 3.5
k_rule = 0.5
k_family = 1.0
k_library = 0.5
k_train = 0.5


def get_intrinsic_correlation(source1, source2):
    # expects the training dictionary
    correlation = 0

    if 'Rate Rules' in source1:
        training1 = source1['Rate Rules'][1]['training']
    elif 'Training' in source1:
        training1 = [(source1['Training'][1].item, source1['Training'][1].item, 1.0)]
    if 'Rate Rules' in source2:
        training2 = source2['Rate Rules'][1]['training']
    elif 'Training' in source2:
        training2 = [(source2['Training'][1].item, source2['Training'][1].item, 1.0)]

    for i in range(0, len(training1)):
        for j in range(0, len(training2)):
            if training1[i][0] == training2[j][0]:
                weight_i = training1[i][2]
                weight_j = training2[j][2]
                correlation += weight_i * weight_j * k_rule
                break
    return correlation


# Construct the covariance matrix
Sigma_k = np.zeros((len(uncertainty.reaction_list), len(uncertainty.reaction_list)))


for i in range(0, len(uncertainty.reaction_list)):
    for j in range(0, i + 1):
        source_entry_i = uncertainty.reaction_sources_dict[uncertainty.reaction_list[i]]
        source_entry_j = uncertainty.reaction_sources_dict[uncertainty.reaction_list[j]]
        if i == j:
            if 'Library' in source_entry_i:
                Sigma_k[i, i] = k_library
            elif 'PDep' in source_entry_i:
                Sigma_k[i, i] = k_library
            elif 'Training' in source_entry_i:
                Sigma_k[i, i] = k_train
            elif 'Rate Rules' in source_entry_i:
                N = len(source_entry_i['Rate Rules'][1]['training'])
                Sigma_k[i, i] = get_intrinsic_correlation(source_entry_i, source_entry_j) + k_family + np.float_power(np.log10(N + 1), 2.0) * k_nonexact
            else:
                raise NotImplementedError

        else:  # off-diagonals
            # If they're library reactions, off diagonal is zero
            if 'Library' in source_entry_i:
                continue
            if 'Library' in source_entry_j:
                continue

            # If they're PDEP, just assume off-diagonal is zero
            if 'PDep' in source_entry_i:
                continue
            if 'PDep' in source_entry_j:
                continue

            # If they're not from the same family, off-diagonal is zero
            if uncertainty.reaction_list[i].family != uncertainty.reaction_list[j].family:
                continue

            intrinsic_corr = get_intrinsic_correlation(source_entry_i, source_entry_j)
            correlation = intrinsic_corr + k_family
            Sigma_k[i, j] = correlation
            Sigma_k[j, i] = correlation


uncorrelated_uncertainties = np.diagonal(Sigma_k)

np.save(os.path.join(this_dir, 'reaction_uncertainty.npy'), uncorrelated_uncertainties)
np.save(os.path.join(this_dir, 'species_uncertainty.npy'), uncertainty.thermo_input_uncertainties)