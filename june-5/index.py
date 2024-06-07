import cv2
import numpy as np
im = cv2.imread("./pattern.jpg")
print(type(im))
print(im.shape)

h, w, c = im.shape

print(f"Image is a {h} x{ w} and of channel {c}")

K = np.array([[1.0, 2.0, 2.0], [2.0, 5.0, 2.0], [1.0, 2.0, 1.0]])
K = K /K.sum()
im2 = cv2.filter2D(im, -1, K)


# cv2.imshow("My randon image", im)
# cv2.waitKey(0)

cv2.imshow("My randon image 2", im2)
cv2.waitKey(0)