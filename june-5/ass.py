import cv2
import numpy as np

patternsImage = cv2.imread("./patterns.png")
carImage = cv2.imread("./lp.jpg")

K1 = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
# With this kernel, the image brightens from pixels of low to high intesity horizontally
K2 = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
# With this kernel, it brightens every vertical dark edge

sharpKernel1 = np.array([
    [0, 0, 0, 0, 0.65], 
    [0, 0, 0, -0.1, 0], 
    [0, 0, -0.02, 0, 0], 
    [0,-0.3, 0, 0, 0],
    [-0.07, 0, 0, 0, 0],
    ])
sharpKernel2 = np.array([
    [0, 0, 0, 0, 0.8], 
    [0, 0, 0, -0.2, 0], 
    [0, 0, -0.02, 0, 0], 
    [0,-0.4, 0, 0, 0],
    [-0.07, 0, 0, 0, 0],
    ])
sharpKernel3 = np.array([
    [0, 0, 0, 0, 0.9], 
    [0, 0, 0, -0.25, 0], 
    [0, 0, -0.02, 0, 0], 
    [0,-0.4, 0, 0, 0],
    [-0.05, 0, 0, 0, 0],
    ])

sharpKernel4 = np.array([
    [0, 0, 0, 0, 0.85], 
    [0, 0, 0, -0.22, 0], 
    [0, 0, -0.021, 0, 0], 
    [0,-0.38, 0, 0, 0],
    [-0.065, 0, 0, 0, 0],
    ])
sharpKernel5 = np.array([
    [0, 0, 0, 0, 0.86], 
    [0, 0, 0, -0.23, 0], 
    [0, 0, -0.022, 0, 0], 
    [0,-0.39, 0, 0, 0],
    [-0.064, 0, 0, 0, 0],
    ])
sharpKernel1 /= sharpKernel1.sum()
sharpKernel2 /= sharpKernel2.sum()
sharpKernel3 /= sharpKernel3.sum()
sharpKernel4 /= sharpKernel4.sum()
sharpKernel5 /= sharpKernel5.sum()

effectViaK1 = cv2.filter2D(patternsImage, -1, K1)
effectviaK2 = cv2.filter2D(patternsImage, -1, K2)
effectOfSharp1 = cv2.filter2D(carImage, -1, sharpKernel1)
effectOfSharp2 = cv2.filter2D(carImage, -1, sharpKernel2)
effectOfSharp3 = cv2.filter2D(carImage, -1, sharpKernel3)
effectOfSharp4 = cv2.filter2D(carImage, -1, sharpKernel4)
effectOfSharp5 = cv2.filter2D(carImage, -1, sharpKernel5)

cv2.imshow("Effect via K1", effectViaK1)
cv2.imshow("Effect via K2", effectviaK2)
cv2.imshow("Effect on sharper 1", effectOfSharp1)
cv2.imshow("Effect on sharper 2", effectOfSharp2)
cv2.imshow("Effect on sharper 3", effectOfSharp3)
cv2.imshow("Effect on sharper 4", effectOfSharp4)
cv2.imshow("Effect on sharper 5", effectOfSharp5)


cv2.waitKey(0)