import numpy as np

# Sample binary matrix (replace this with your binary matrix)
binary_matrix = np.array([
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 1, 0, 0, 0],
    [1, 1, 1, 0, 0],
    [0, 0, 0, 1, 1]
])

# Feature extraction
num_rows, num_cols = binary_matrix.shape
total_pixels = num_rows * num_cols
num_ones = np.sum(binary_matrix)
density = num_ones / total_pixels
vertical_sum = np.sum(binary_matrix, axis=0)
horizontal_sum = np.sum(binary_matrix, axis=1)
num_vertical_lines = np.sum(vertical_sum > 0)
num_horizontal_lines = np.sum(horizontal_sum > 0)

# Print extracted features
print("Density:", density)
print("Number of ones:", num_ones)
print("Number of vertical lines:", num_vertical_lines)
print("Number of horizontal lines:", num_horizontal_lines)
