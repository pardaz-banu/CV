import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("capture_isp_3.png")
grayScaleImg = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
grayImg = np.float32(grayScaleImg)
dest = cv2.cornerHarris(grayImg,8, 29, 0.05) # find Harris corners
dest = cv2.dilate(dest, None)
image[dest > 0.01 * dest.max()]=[0, 0, 255]
cv2.imshow('Image with Corners', image)
cv2.imwrite("cornersImage.png",image)
plt.imshow(image)
plt.show()