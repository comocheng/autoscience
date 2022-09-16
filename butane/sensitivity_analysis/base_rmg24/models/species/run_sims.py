import sys

sys.path.append('/work/westgroup/harris.se/autoscience/autoscience/utils')
import simulation


cti_file = sys.argv[1]
delay = simulation.get_delay(cti_file)
result_file = f'delay_{cti_file[-8:-4]}.txt'
with open(result_file, 'w') as f:
    f.write(str(delay))

