import cv2
import numpy as np
img=cv2.imread("image/colour.jpg")
cv2.imshow("Kids",img)
b,g,r=cv2.split(img)
cv2.imshow('blue',b)
cv2.imshow('green',g)
cv2.imshow('red',r)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)
merged=cv2.merge([b,g,r])
cv2.imshow("Merged",merged)
cv2.waitKey(0)

