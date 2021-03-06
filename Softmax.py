"""Softmax."""

scores = [3.0, 1.0, 0.2]


import numpy as np
#np.set_printoptions(precision=8)
scores = np.array([[1, 2, 3, 6],
                   [2, 4, 5, 6],
                   [3, 8, 7, 6]])

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    x = np.array(x)
    result = np.array(x.shape)  # TODO: Compute and return softmax(x)
    result = np.exp(x)/np.sum(np.exp(x), axis=0)
    return result

print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
