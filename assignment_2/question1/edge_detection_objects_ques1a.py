import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("capture_isp_1.png")
cannyEdge_image = cv2.Canny(image,180,200) #canny edge detection
print(image)
plt.imshow(image)
cv2.imwrite("cannyEdgeOutput.png",cannyEdge_image)
plt.imshow(cannyEdge_image,cmap="gray")
plt.show()