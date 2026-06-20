import numpy as np

# calculate the determinat and inverse of a 3X3 matrix
A = np.array([[1,2,3], [4,5,20], [3,4,5]])

# determinat
det = np.linalg.det(A)
# print("Determinat: \n", det)

inv = np.linalg.inv(A)
# print("Inverse: \n", inv)

# calculate eigenvalue and eigenvector
eigValue, eigVector = np.linalg.eig(A)
# print("Eigen Value: \n", eigValue)
# print("Eigen Vector: \n", eigVector)

U, S, Vt = np.linalg.svd(A)
# print("U: \n", U)
# print("Singular value \n", S)
# print("V transpose: \n", Vt)