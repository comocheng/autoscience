# script to revise the RMG Disproportionation training reactions

# imports
import os
import rmgpy
import rmgpy.data.kinetics


# load the calculated training reactions
# load all of the kinetics calculations
this_file = os.path.abspath(__file__)
DFT_DIR = os.path.join(os.path.dirname(this_file), '..', '..', 'butane', 'dft')

kinetics_dir = os.path.join(DFT_DIR, 'kinetics', 'kinetics')
ark_kinetics_database = rmgpy.data.kinetics.KineticsDatabase()
ark_kinetics_database.load_libraries(kinetics_dir)
print(f'{len(ark_kinetics_database.libraries[""].entries)} new reactions loaded')

# Load the existing library

# load the revised Disproportionation family
family = 'Disproportionation'
ref_library_path = os.path.join(rmgpy.settings['database.directory'], 'kinetics')
rmg_kinetics_database = rmgpy.data.kinetics.KineticsDatabase()
rmg_kinetics_database.load(
    ref_library_path,
    libraries=[],
    families=[family]
)
training_depo = rmg_kinetics_database.families['Disproportionation'].get_training_depository()


changed = 0
no_rank = 0
for key in training_depo.entries:
    # make sure the rank is 10 or 11
    if not training_depo.entries[key].rank:
        # print(f'No rank for {training_depo.entries[key]}')
        no_rank += 1
        continue

    if training_depo.entries[key].rank < 10:
        continue

    for arkane_key in ark_kinetics_database.libraries[""].entries:
        if training_depo.entries[key].item.is_isomorphic(ark_kinetics_database.libraries[""].entries[arkane_key].item):
            training_depo.entries[key].data = ark_kinetics_database.libraries[""].entries[arkane_key].data
            print(f'Replacing training data for {training_depo.entries[key]}')
            changed += 1
            break

print(f'No rank for {no_rank} reactions')
print(f'Changed {changed} reactions')


# check how many of training reactions are repeats
duplicates = 0
for key1 in training_depo.entries:
    for key2 in training_depo.entries:
        if key1 == key2:
            continue

        if training_depo.entries[key1].item.is_isomorphic(training_depo.entries[key2].item):
            duplicates += 1
            print(f'{key1} and {key2} are duplicates')

print(f'There are {duplicates} duplicate training reactions')


# save the new library
# Save the results over the previous reaction.py
training_dir = os.path.join(rmgpy.settings['database.directory'], 'kinetics', 'families', family, 'training')
training_depo.save(os.path.join(training_dir, 'reactions.py'))
print('Saved new training reactions')
