# exercise
import numpy as np

# brocasting execrise
# 1. create a 3x3 matrix and add 1x3 vector to it and then multiply the matrix by scalar
arr1 = np.array([[1,2,4], [3,4,5], [5,6,7]])
# print("3x3 array: ", arr1)
vec1 = np.random.randint(1,10, size=(1,3))
# print("1x3 vector: ",vec1)
arr1 += vec1
# print("addition: ", arr1)

arr1 *= 2
# print("multiply by scalar: ", arr1)

# generating and filtering a random dataset
# 2. create a 5x5 martix of random integers 1 and 50 and filter values greater than 25 and 
# replace them with zero and then calcuate the sum, mean and std of the modified matrix

# generating the matrix
gen_arr = np.random.randint(1,50, size=(5,5))
print("Generated random dataset: \n", gen_arr)

# filtering
gen_arr[gen_arr > 25] = 0
print("Filtered and replaced array: \n", gen_arr)

# calculation
arr_sum = np.sum(gen_arr)
print("sum: \n", arr_sum)

arr_mean = np.mean(arr_sum)
print("mean: \n", arr_mean)

arr_std = np.std(arr_mean)
print("std: \n", arr_std)


