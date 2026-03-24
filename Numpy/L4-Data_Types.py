import numpy as np

x = np.array([1,2,3,4,5], dtype='U')

print(x)
print(x.dtype)

y = x.astype('f')
print(y)
print(y.dtype)