# script to check the vibrational frequency a transition state
import os
import sys
import glob

import autotst.calculator.vibrational_analysis


DFT_DIR = "/work/westgroup/harris.se/autoscience/autoscience/butane/dft/"
# DFT_DIR = "/home/moon/autoscience/autoscience/butane/dft/"

reaction_index = int(sys.argv[1])
# reaction_index = 288
# reaction_index = 1721

result_file = os.path.join(
    DFT_DIR, 'kinetics', f'reaction_{reaction_index:04}', 'arkane', 'vibrational_analysis_check.txt'
)

reaction_logfiles = glob.glob(
    os.path.join(DFT_DIR, 'kinetics', f'reaction_{reaction_index:04}', 'arkane', 'fwd_*.log')
)
assert len(reaction_logfiles) == 1
reaction_logfile = reaction_logfiles[0]

# get the reaction smiles
os.environ['DFT_DIR'] = DFT_DIR
#sys.path.append('/home/moon/autoscience/autoscience_workflow/workflow/scripts/kinetics')
sys.path.append('/work/westgroup/harris.se/autoscience/autoscience_workflow/workflow/scripts/kinetics')
import kineticfun

reaction_smiles = kineticfun.reaction_index2smiles(reaction_index)
reaction = autotst.reaction.Reaction(label=reaction_smiles)
va = autotst.calculator.vibrational_analysis.VibrationalAnalysis(
    transitionstate=reaction.ts['forward'][0], log_file=reaction_logfile
)
result = va.validate_ts()

print(result)

# write the result to a file
with open(result_file, 'w') as f:
    f.write(str(result))

