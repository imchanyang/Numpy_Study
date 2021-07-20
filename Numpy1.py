import numpy as np

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.concatenate([array1, array2])

print(array3)
print(array3.shape)


array4 = np.array([1, 2, 3, 4])
array5 = array4.reshape((2, 2))
print(array4)
print(array5)

array_1 = np.arange(4).reshape(1, 4)
array_2 = np.arange(8).reshape(2, 4)
array6 = np.concatenate([array_1, array_2], axis=0)
print(array6)

array = np.arange(8).reshape(2, 4)
left, right = np.split(array, [2], axis=1)
print(array)
print(left)
print(right)