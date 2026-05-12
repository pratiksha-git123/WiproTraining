import numpy
import numpy as np

np.random.seed(42)
data_array = np.random.randint(1, 501, size = (10,10))

print("Original Array:\n", data_array)

global_mean = np.mean(data_array)
modified_array = np.where(data_array > global_mean, 0, data_array)
print("\n Global Mean:\n", global_mean)
print("\n Modified Array:\n", modified_array)

column_sums = np.sum(modified_array, axis=0)
row_std = np.std(modified_array, axis=1)
print("\n Column Sums:\n", column_sums)
print("\n Row standard deviations:\n", row_std)

center_matrix = modified_array[3:7, 3:7]
flat_array = center_matrix.flatten()
print("\n Center 4*4 Submatrix:\n", center_matrix)
print("\n Flattened 1D array:\n", flat_array)


