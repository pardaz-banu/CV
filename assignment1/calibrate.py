import numpy as np
import cv2 as cv
import glob

from scipy.spatial.transform import Rotation
from math import cos, sin, radians

# def trig(angle):
#     r = radians(angle)
#     return cos(r), sin(r)

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
images = glob.glob('*.png')
for fname in images:
    img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (7,6), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (7,6), corners2, ret)
        cv.imshow('img', img)
        cv.waitKey(500)

#print(objpoints)
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
#print(mtx)
cv.destroyAllWindows()

print(mtx)
#mtx is a intrinsic matrix
#we have to convert the above intrinsic mtx matrix to 4x4 and have to find the extrinsic matrix
#to find the extrinsic matrix we have to do rotation and then translation
#extrinsic matrix = dot product of rotation and translation matrix
#final camera matrix = dot product of intrinsic and extrinsic matrix

