import cv2
import numpy as np
image=cv2.imread("image/cameraman.tif")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gray,(5,5),0)
edge=cv2.Canny(blurred,50,150)
cv2.imshow("Original",image)
cv2.imshow("edges",edge)
cv2.waitKey(0)
cv2.destroyAllWindows()