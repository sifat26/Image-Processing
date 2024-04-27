import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img=cv.imread('image/cameraman.tif',0)
cv.imshow("Image",img)
plt.hist(img.ravel(),256,[0,256])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()