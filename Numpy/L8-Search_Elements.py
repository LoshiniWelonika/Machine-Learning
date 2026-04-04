import numpy as np

arr = np.array([1,3,4,6,7])

#Searching Elements 
x = np.where(arr==4)
y = np.where(arr%2==0)

print(x)  
print(y) 
print(np.searchsorted(arr,[2,5,8]))