import os
import rmgpy.data.kinetics


# Load the new kinetics library
DFT_DIR = "/work/westgroup/harris.se/autoscience/autoscience/butane/dft/"
DFT_DIR = "/home/moon/autoscience/autoscience/butane/dft/"
kinetics_lib = os.path.join(DFT_DIR, 'kinetics', 'kinetics')
ark_kinetics_database = rmgpy.data.kinetics.KineticsDatabase()
ark_kinetics_database.load_libraries(kinetics_lib)
print(f'{len(ark_kinetics_database.libraries[""].entries)} entries loaded')


for T in [350, 1000, 5000]:
    for entry in ark_kinetics_database.libraries[""].entries:
        rate = ark_kinetics_database.libraries[""].entries[entry].data.get_rate_coefficient(T, 101325)
        if rate > 10 ** 25:
            print(entry)
