# Exe_1: create a vector and matrixes using numpy
import numpy as np

vector = np.array([1,2,4])
print("Vector: \n", vector)

A = np.array([[1,2,4,5], [1,2,3,4], [1,2,4,5]])
print("Matrix: \n", A)

B = np.array([[3,2,8,7], [3,4,5,72], [3,4,5,8]])

# and matrix operation
# Addition
print(A+B)
# Subtraction
print(A-B)
# scalar product
print(2*A)
# cross product
print(np.dot(A,B))

# Exe_2: Implement Matrix-Vector multiplication
print(np.dot(vector, A))