# exercise
import numpy as np

# 1. create a 3x3 matrix and add 1x3 vector to it and then multiply the matrix by scalar
arr1 = np.array([[1,2,4], [3,4,5], [5,6,7]])
print("3x3 array: ", arr1)
vec1 = np.random.randint(1,10, size=(1,3))
print("1x3 vector: ",vec1)
arr1 += vec1
print("addition: ", arr1)

arr1 *= 2
print("multiply by scalar: ", arr1)

# 2. 