import cv2
img1=cv2.imread("image/kids.tif",cv2.IMREAD_COLOR)
img2=cv2.GaussianBlur(img1,(15,15),0)

cv2.imshow("Input Image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()