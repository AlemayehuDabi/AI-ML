# working with numpy arrays
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(type(arr))

zeros = np.zeros((3, 3))
# print(zeros)

ones = np.ones((3, 3))
# print(ones)

twos = np.full((3, 3), 2)
# print(twos)


# working with arange
arr = np.arange(1,10,2)
# print(arr)

lin_space = np.linspace(1,10,5)
# print(lin_space)


# manipulating array
# changing the shape
arr_reshape = [1,2,3,4,5,6] 
reshape = np.reshape(arr_reshape, (2,3)) # caution here you need to cal the array size and it should match the resize
# print(reshape)


a = np.arange(6).reshape((3, 2))
# print(a)

new_axis = a[:, np.newaxis]
# print(new_axis)