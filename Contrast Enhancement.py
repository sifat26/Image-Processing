import cv2
gray_image=cv2.imread('image/kids.tif',cv2.IMREAD_GRAYSCALE)
equalized_image=cv2.equalizeHist(gray_image)
cv2.imshow("Original Image",gray_image)
cv2.imshow("Equalized Image",equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()