import cv2
noisy_image=cv2.imread('image/noisi.jpg')
denoised_image=cv2.GaussianBlur(noisy_image,(5,5),0)
cv2.imshow('Noisy Image',noisy_image)
cv2.imshow('Denoised Image',denoised_image)
cv2.waitKey(0)
cv2.destroyAllWindows()