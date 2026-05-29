import numpy as np

arr = np.array([1,3,4,5,6,7,8])

# boolean indexing and filtering using var
even_arr = arr[arr % 2 == 0]

print("Even array: ", even_arr)

# modifing - replacing every element greater then 2
arr[arr > 2] = 0
print("Modified Arr: ", arr)