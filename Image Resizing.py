import cv2
image=cv2.imread("image/horse.webp",cv2.IMREAD_COLOR)
resized=cv2.resize(image,(300,300))

cv2.imshow("Resized Image",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()