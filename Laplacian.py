import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('image/lena_color.tiff', cv2.IMREAD_GRAYSCALE)

# Apply the Laplacian filter
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# Convert the result to unsigned 8-bit integer (if needed)
laplacian = np.uint8(np.absolute(laplacian))

# Display the original and filtered images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian Filtered Image')
plt.axis('off')

plt.show()
