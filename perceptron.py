import numpy as np
train = np.array([[0,0,1], [0,1,1], [1,0,1], [1,1,1]])
d = np.array([[-1,-1,1,1]])
eta = 0.5

w_old = np.array([[0.0, 0.0, 0.0]])
w_new = np.array([[0.0, 0.0, 0.0]])
count = 0

while True:
    y = np.dot(w_new, np.transpose(train))
    y[y < 0] = -1
    y[y >= 0] = 1
    error = d - y
    w_new = w_old + eta * np.dot(error, train)
    
    if not np.array_equal(w_new, w_old):
        print('iteration:', count, w_new)
        w_old = w_new
        count += 1
    else:
        break
    
result = np.dot(w_new, np.transpose(train)) 
print('final dot', result)