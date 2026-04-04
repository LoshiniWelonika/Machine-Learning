import numpy as np

arr1 = np.array([[1,2,3],[7,8,9]])
arr2 = np.array([[4,5,6],[3,4,5]])

newarr = np.concatenate((arr1,arr2),axis=1)
print(newarr) 


#Spliting an array
arr3 = np.array([1,2,3,4,5,9])

splitedArray = np.array_split(arr3,4)
print(splitedArray)