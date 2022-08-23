import os
import glob

import arkane.ess.gaussian
from arkane.exceptions import LogError


DFT_DIR = "/work/westgroup/harris.se/autoscience/autoscience/butane/dft/"


kinetics_dir = os.path.join(DFT_DIR, 'kinetics')


not_started_overall = set()
incomplete_shell = set()
incomplete_overall = set()


reaction_dirs = glob.glob(os.path.join(kinetics_dir, 'reaction_*'))

for reaction_dir in reaction_dirs:
    reaction_index = int(reaction_dir[-4:])
    shell_dir = os.path.join(reaction_dir, 'shell')
    shell_slurm_scripts = glob.glob(os.path.join(shell_dir, 'run_*.sh'))
    N_shell = len(shell_slurm_scripts)

    shell_logfiles = glob.glob(os.path.join(shell_dir, '*ts_*.log'))
    # if len(shell_logfiles) == 0:
    #     continue

    if len(shell_logfiles) != N_shell:
        print(f'Incorrect number of shell logfiles for {reaction_index}')

    # check for files that didn't run
    for logfile in shell_logfiles:
        if not os.path.exists(logfile):
            print(f'Missing path {logfile}')
            continue

        try:
            g_reader = arkane.ess.gaussian.GaussianLog(logfile)
            g_reader.check_for_errors()
        except LogError:
            print(f'Incomplete shell log {logfile}')
            incomplete_shell.add(reaction_index)

    # check for overall calculations
    overall_dir = os.path.join(reaction_dir, 'overall')
    overall_slurm_scripts = glob.glob(os.path.join(overall_dir, 'run_*.sh'))
    N_overall = len(overall_slurm_scripts)

    overall_logfiles = glob.glob(os.path.join(overall_dir, '*ts_*.log'))
    if len(overall_logfiles) == 0:
        not_started_overall.add(reaction_index)
        continue

    if len(overall_logfiles) != N_overall:
        print(f'Incorrect number of overall logfiles for {reaction_index}')

    # check for files that didn't run
    for logfile in overall_logfiles:
        if not os.path.exists(logfile):
            print(f'Missing path {logfile}')
            continue

        try:
            g_reader = arkane.ess.gaussian.GaussianLog(logfile)
            g_reader.check_for_errors()
        except LogError:
            print(f'Incomplete overall log {logfile}')
            incomplete_overall.add(reaction_index)


print('\nIncomplete shell calcs:')
for incomplete in incomplete_shell:
    print(incomplete)

print('\nIncomplete overall calcs:')
for incomplete in incomplete_overall:
    print(incomplete)

print('\nNot started overall calcs:')
for incomplete in not_started_overall:
    print(incomplete)
