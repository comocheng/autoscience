import os
import pickle

import numpy as np
import rmgpy.chemkin

# Load the model and the saved uncertainty covariance matrix.
# Only looks at uncorrelated parameters, so you can fill the
# diagonal of a zero matrix and get the same results as using
# the full covariance matrix

basedir = '/work/westgroup/harris.se/autoscience/autoscience/butane/rmg_model'
model_dir = '/scratch/harris.se/autoscience/uncorrelated/models'  # where the output cti's go

base_chemkin = os.path.join(basedir, 'chem_annotated.inp')
dictionary = os.path.join(basedir, 'species_dictionary.txt')
transport = os.path.join(basedir, 'tran.dat')
# RMG_cti_path = os.path.join(basedir, 'chem_annotated.cti')

species_list, reaction_list = rmgpy.chemkin.load_chemkin_file(base_chemkin, dictionary_path=dictionary, transport_path=transport)
# RMG_gas = ct.Solution(RMG_cti_path)


covariance_file = '/work/westgroup/harris.se/autoscience/autoscience/uncertainty/butane_covariance.pickle'
with open(covariance_file, 'rb') as handle:
    Sigma_k = pickle.load(handle)

# Generate the random numbers
np.random.seed(400)
mean_vec = np.zeros(Sigma_k.shape[0])  # Sigma_k is a square matrix
N = 5000
normal_randoms = np.random.multivariate_normal(mean_vec, Sigma_k, size=N)


# compute the CDF
sorted_normals = np.sort(normal_randoms, axis=0)
CDF = np.zeros(sorted_normals.shape)
for rxn_index in range(0, sorted_normals.shape[1]):
    # the variance represents the 1/12*(b-a)^2
    # the variance represents the a^2/3
    var = Sigma_k[rxn_index, rxn_index]
    a = np.sqrt(3 * var)  # assumed uniform distribution is symmetric about zero
    CDF[:, rxn_index] = np.linspace(-a, a, sorted_normals.shape[0])


# function to actually convert the normal randoms into uniform randoms
def normal_to_uniform(sample, rxn_index):
    # assumes CDF is already defined
    # find the closest value to the input
    distance = np.abs(sorted_normals[:, rxn_index] - sample)
    closest_index = np.argmin(distance)
    return CDF[closest_index, rxn_index]


# convert all those normal variables to uniforms
uniform_randoms = np.zeros(normal_randoms.shape)
for i in range(0, normal_randoms.shape[0]):
    for j in range(0, normal_randoms.shape[1]):
        uniform_randoms[i, j] = normal_to_uniform(normal_randoms[i, j], j)
np.save('uniform_randoms.npy', uniform_randoms)

