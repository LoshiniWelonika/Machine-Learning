import numpy as np

arr = np.array([[[1,2],[3,4]], [[5,6],[7,8]]]) 

arr2 = np.array([1,2,3,4], ndmin=5)

print(arr)
print("")
print(arr2)
print("")

print(arr.shape)

print(arr2.shape)
print("")


print("Reshape")
arr3 = np.array([1,2,3,4,5,6,7,8,9])
print(arr3)
new = arr3.reshape(3,3)
print(new) 


#Converting multi dimensional array into q 1D array 
new2 = arr.reshape(-1)
print(new2)
