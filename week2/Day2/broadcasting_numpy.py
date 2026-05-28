import numpy as np

# broadcasting w/ the same dimension
arr1 = np.array([[1,2,4]])
arr2 = np.array([5,6,7])

# broadcasting w/ different dimension
# one of the dimension is 1
arr3  = np.array([[3,5,6,7], [2,3,4,5]])
arr4 = np.array([3,19,23,45])

# print(arr1 + arr2)
print(arr3 + arr4)