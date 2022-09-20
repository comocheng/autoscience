import os
import sys
kinetic_module_path = '/work/westgroup/harris.se/autoscience/autoscience_workflow/workflow/scripts/kinetics'
sys.path.append(kinetic_module_path)
import kineticfun


reaction_index = sys.argv[1]


complete = kineticfun.shell_complete(reaction_index)
print(complete)

