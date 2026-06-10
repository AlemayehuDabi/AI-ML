import numpy as np

A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])

# matrix addition
# print("Addition: \n", A+B)
# matrix subtraction
# print("Subtraction: \n", A-B)

# scalar muliptication
C = 2 * A
# print("Mulitplication: \n", C)

# Cross product - there is a method called dot for this.
cross_product = np.dot(A,B)
# print(cross_product)
# A*B is not cross product but instead this is multiplication 


# identity matrix
I = np.eye(3)
# print("Identity Matrix: \n", I)

# Zero matrix
Z = np.zeros((4,3))
# print("Zero Matrix: \n", Z)

# diagonal matrix
D = np.diag([1,2,4,5])
# print("Diagnoal Matrix: \n", D)