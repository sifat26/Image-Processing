import cv2
img = cv2.imread("image/kids.tif",0)
row=img.shape[0]
col=img.shape[1]
##binary=img.copy()
negative=img.copy()
for i in range (row):
    for j in range (col):
        negative[i][j]=255 - negative[i][j]

cv2.imshow("Input Image",img)
cv2.imshow("Negative Image",negative)
cv2.waitKey(0)
cv2.destroyAllWindows()