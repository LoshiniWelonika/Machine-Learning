import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9])
print(x[1:4])

print(x[-7:-4])

print(x[2:])

print(x[:4])

print(x[1::2])
print("")


y = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(y[1,1:])

print(y[:,2])
