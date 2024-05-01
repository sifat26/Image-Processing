import numpy as np
import matplotlib.pyplot as plt
from skimage import data
from skimage.filters import threshold_otsu
from skimage.segmentation import clear_border
from skimage.measure import label, regionprops
from skimage.morphology import closing, square
from skimage.color import label2rgb

# Load a sample image
image = data.coins()

# Convert the image to grayscale
gray_image = image[:, :, 0]

# Apply Otsu's thresholding method to segment the image
thresh = threshold_otsu(gray_image)
binary_image = gray_image > thresh

# Remove small white regions and small black holes using morphological operations
binary_image = closing(binary_image, square(3))
cleared = clear_border(binary_image)

# Label connected components in the binary image
label_image = label(cleared)

# Get properties of labeled regions
regions = regionprops(label_image)

# Display the original image with segmented regions outlined
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(label2rgb(label_image, image=image, bg_label=0))
plt.title('Segmented Image')
plt.axis('off')

plt.show()
