import numpy as np

A = np.array([[12,23,99],[34,56,22]])


U, S, Vt = np.linalg.svd(A)
print("U: \n", U)
print("Singular value: \n", S)
print("V transpose: \n", Vt)
