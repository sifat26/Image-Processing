import cv2
import numpy as np

# Load an image
image = cv2.imread('image/lena_color.tiff')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a threshold to the grayscale image to convert it to binary
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Convert binary image to binary matrix
binary_matrix = (binary_image / 255).astype(np.uint8)

# Print the binary matrix
print(binary_matrix)
