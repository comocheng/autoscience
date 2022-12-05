# Script for running a single arkane thermo job
import sys
sys.path.append('/work/westgroup/harris.se/autoscience/autoscience_workflow/workflow/scripts/thermo')
import job  # TODO rename this to something more descriptive


species_index = int(sys.argv[1])
species_smiles = job.index2smiles(species_index)
print(species_smiles)

if job.arkane_complete(species_index):
    print("Skipping because complete")
    exit(0)

print("Running Arkane")
job.run_arkane_job(species_index)
print("CALCULATION COMPLETE")

