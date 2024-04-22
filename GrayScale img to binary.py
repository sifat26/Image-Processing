import cv2
img = cv2.imread("image/kids.tif",0)
row=img.shape[0]
col=img.shape[1]
binary=img.copy()
for i in range (row):
    for j in range (col):
        pixel=binary[i][j]
        if pixel > 120:
            binary[i][j]=255
        else:
            binary[i][j]=0
cv2.imshow("Input Image",img)
cv2.imshow("Binary Image",binary)
cv2.waitKey(0)
cv2.destroyAllWindows()