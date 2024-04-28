import cv2
image=cv2.imread("image/horse.webp",cv2.IMREAD_COLOR)
normalized_image = (image - image.mean()) / image.std()

cv2.imshow("Resized Image",normalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()