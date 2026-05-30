import numpy as np

# setting random seed
np.random.seed(42) # legacy way

rand_arr = np.random.rand(3,4)
print("Random Array: \n", rand_arr)

rand_arr_int = np.random.randint(0,10, size=(2,3))
print("Random Array Int: \n", rand_arr_int)


rng = np.random.default_rng(seed=42) # modern style

rand_arr2  = rng.random(size=(3,3))
print("Randon arr 2: \n", rand_arr2)


rand_arr3  = rng.integers(1,10,size=(3,3))
print("Randon arr 2: \n", rand_arr3)