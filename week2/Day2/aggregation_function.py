import numpy as np

arr = np.array([[1,2,4,5], [6,7,8,9]])

# aggregation function
print("Sum: ", np.sum(arr))
print("Mean: ", np.mean(arr))
print("Max: ", np.max(arr))
print("Min: ", np.min(arr))
print("Standard Deviation: ", np.std(arr))
print("Sum along a row: ", np.sum(arr, axis=1))
print("Sum along a column: ", np.sum(arr, axis=0))
