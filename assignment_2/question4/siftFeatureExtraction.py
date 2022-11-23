import cv2
import numpy as np
import matplotlib.pyplot as plt
from random import randrange

img_ = cv2.imread("../question1/capture_isp_1.png")
img1 = cv2.cvtColor(img_,cv2.COLOR_BGR2GRAY)
img = cv2.imread("../question1/capture_isp_2.png")
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
# find the keypoints and descriptors with SIFT
k1, des1 = sift.detectAndCompute(img1,None)
k2, des2 = sift.detectAndCompute(img2,None)

bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)
g = []
for m in matches: 
    if m[0].distance < 0.5*m[1].distance:
        g.append(m)
    matches = np.asarray(g)

if len(matches[:,0]) >= 4:
    src = np.float32([ k1[m.queryIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    dst = np.float32([ k2[m.trainIdx].pt for m in matches[:,0] ]).reshape(-1,1,2)
    H, masked = cv2.findHomography(src, dst, cv2.RANSAC, 5.0)
    #print H
else:
    print("Can't find enough keypoints.")

dest = cv2.warpPerspective(img_,H,(img.shape[1] + img_.shape[1], img.shape[0]))
plt.subplot(122),plt.imshow(dst),plt.title("Warped Image")
plt.show()
plt.figure()
dest[0:img.shape[0], 0:img.shape[1]] = img
cv2.imwrite("output.jpg",dest)
plt.imshow(dst)
plt.show()