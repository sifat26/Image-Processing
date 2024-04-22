import cv2
import numpy as np
img1=cv2.imread("image/kids.tif",cv2.IMREAD_GRAYSCALE)
height =img1.shape[0]
width=img1.shape[1]
img2=np.zeros((height,width,3),'uint8')
img3=img1.copy();
for i in range (height):
    for j in range (width):
        img2[i][j] = img1[i][j]
cv2.imshow("Input Image",img1)
cv2.imshow("Output Image",img2)
cv2.imshow("Output Image3",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()