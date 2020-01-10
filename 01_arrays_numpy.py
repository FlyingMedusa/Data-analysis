import numpy as np

array1 = np.arange(1, 26)
array1 = array1.reshape(5,5)
print(array1)

array2 = array1[2:, 1:]
print("\n", array2)

selecting_20 = array1[3, 4]
print("\n", selecting_20)

array3 = array1[:3, 1]
array3 = array3.reshape(3, 1)
print("\n", array3)

all_elem_sum = array1.sum()
print("\n", all_elem_sum)

col_sum = array1.sum(axis=0)
print("\n", col_sum)

