import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

x = np.loadtxt('input/data1.txt')

# number of mixtures
M = 3
# likelihood of the mixture
alpha = np.ones(M)*(1/M)
# Intitialize means randomly
mu = np.random.random(M)*20 
# Intitialize sd randomly
sigma = np.ones(M)*100.0 

weight = np.zeros((M, len(x)))

for i in range(100): 
	
	L = 0
	for j in range(M):
		weight[j] = alpha[j] * mlab.normpdf(x, mu[j], sigma[j])

	# calculate new class priors
	alpha = np.sum(weight, axis=1)/len(x)
	mu = np.sum(weight*x, axis=1)/np.sum(weight, axis=1)
	sigma = np.sqrt(np.sum(weight * pow(x - mu[:,np.newaxis],2), axis=1) / np.sum(weight, axis=1))

	# Log likelihood
	#ToDo
