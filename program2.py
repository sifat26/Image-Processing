import cv2
img1=cv2.imread("image/kids.tif",cv2.IMREAD_COLOR)
img2=cv2.imread("image/kids.tif",cv2.IMREAD_GRAYSCALE)
##for color image - row,column,chanel
print(img1.shape)
##for grayscale-image- row,column
print(img2.shape)
## count image pixel
print(img1.size)
# Image datatype
print(img1.dtype)
cv2.imshow("Input Image",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()