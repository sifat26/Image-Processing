import cv2
img1=cv2.imread("image/kids.tif",cv2.IMREAD_COLOR)
img2=cv2.imread("image/kids.tif",cv2.IMREAD_GRAYSCALE)
img3=cv2.imread("image/kids.tif",1)
img4=cv2.imread("image/kids.tif",2)

cv2.imshow("Input Image",img4)
cv2.waitKey(0)
cv2.destroyAllWindows()