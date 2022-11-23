import cv2
import numpy as np
import matplotlib.pyplot as plt

# D = 40
# T = 30
# This is by manual distance measure

img1 = cv2.imread('marker_pos1.png', 0) 
img2 = cv2.imread('marker_pos2.png', 0)

def ShowDisparity(bSize=5):
    stereo = cv2.StereoBM_create(numDisparities=32, blockSize=bSize) 
    disparity = stereo.compute(img1, img2)
    min = disparity.min()
    max = disparity.max()
    disparity = np.uint8(255 * (disparity - min) / (max - min)) 
    return disparity


result = ShowDisparity(bSize=5) 
print(result) 
plt.imshow(result, 'gray') 
cv2.imwrite("output.png", result)
plt.axis('off')
plt.show()

# result = showDisparity(img1, img2, bSize=5)
# print(result)
# plt.imshow(result, 'gray')
# plt.axis('off')
# plt.show()