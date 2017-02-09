import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

x = np.loadtxt(data1.txt)

# number of mixtures
M = 3 
# likelihood of the mixture
alpha = np.ones(M)*(1/M)
# Intitialize means randomly
mu = np.random.random(M)*50 
# Intitialize sd randomly
sigma = np.ones(M)*100.0 

weight = np.zeros((M, len(x)))

for i in range(50):
	print('alpha:', alpha, 'mu:', mu, 'sigma', sigma)
	L = 0
	for j in range(M):
		expectation()
	
	maximization()
	for k in range(len(x)):
		L += log(np.sum(weight, axis=1))
	print('Log likelihood:', L)
	
	
def expectation():
	weight[m] = weight[m] = alpha[m] * mlab.normpdf(x, mu[m], sigma[m])
	
	
def maximization():
	mu = np.sum(weight*x, axis=1)/np.sum(weight, axis=1)	
	sigma = np.sqrt(np.sum(weight * pow(x - mu[:,np.newaxis],2), axis=1) / np.sum(weight, axis=1))
	
	#calculate new class priors
	alpha = np.sum(weight, axis=1)/len(x)
	

