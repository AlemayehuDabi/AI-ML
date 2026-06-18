# egien values and vectors
import numpy as np

A = np.array([[1,2],[3,2]])

eigenValues, eigenVectors = np.linalg.eig(A)
# print("Eigen values: ", eigenValues)
# print("Eigen vectors: ", eigenVectors)