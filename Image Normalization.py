import cv2
import numpy as np
image=cv2.imread('image/kids.tif')
normalized_image=image.astype(np.float32)/255.0
cv2.imshow("Original Image",image)
cv2.imshow('Normalized IMage',normalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
