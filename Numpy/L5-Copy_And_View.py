import numpy as np

x = np.array([1,2,3,4,5])

y = x.copy()
z = x.view()

x[0] = 9

print(x)
print(y)
print(z)