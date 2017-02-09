import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

x = np.loadtxt('data1.txt')

# number of mixtures
m = 3
n = m-1
# likelihood of the mixture
alpha = np.ones(m)*(1/m)
# Intitialize means randomly
mu = np.random.random(m)*50 
# Intitialize sd randomly
sigma = np.ones(m)*100.0 

weight = np.zeros((m, len(x)))

def expectation():
	weight[n] = weight[n] = alpha[n] * mlab.normpdf(x, mu[n], sigma[n])

def maximization():
	mu = np.sum(weight*x, axis=1)/np.sum(weight, axis=1)
	sigma = np.sqrt(np.sum(weight * pow(x - mu[:,np.newaxis],2), axis=1) / np.sum(weight, axis=1))

	#calculate new class priors
	alpha = np.sum(weight, axis=1)/len(x)

for i in range(50):
	print('alpha:', alpha, 'mu:', mu, 'sigma', sigma)
	L = 0
	for j in range(m):
		expectation()
	maximization()
    
	for k in range(len(x)):
		L += np.log(np.sum(weight, axis=1))
	print('Log likelihood:', L)




