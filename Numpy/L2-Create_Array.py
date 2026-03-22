import numpy as np

x = np.array([2, 4, 56, 7, 98])
print(x)
print(x.ndim)
print("\n")
print(x[0])

twodArray = np.array([[1,2,3,4], [5,6,7,8]])
print(twodArray)
print(twodArray.ndim)
print("\n")

threedArray = np.array([[[1,2],[3,4]], [[5,6],[7,8]]])
print(threedArray)
print(threedArray.ndim)
print(threedArray[1,0,1])
print("\n")

fourdArray = np.array([1,2,3,4], ndmin=4)
print(fourdArray)
print(fourdArray.ndim)
print("\n")

print("Array Indexing")
print(twodArray[1,0])