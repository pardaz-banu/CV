import numpy as np
import cv2

imagesPaths1 = ["./stitching_images/secondSet/rialto1.jpeg","./stitching_images/secondSet/rialto2.jpeg","./stitching_images/secondSet/rialto3.jpeg"]
imagesPaths2 = ["./stitchingImages/studentcentereast1.jpg","./stitchingImages/studentcentereast2.jpg","./stitchingImages/studentcentereast3.jpg","./stitchingImages/studentcentereast4.jpg"]
imagesPaths3 = ["./stitchingImages/sciencecenter1.jpg","./stitchingImages/sciencecenter2.jpg","./stitchingImages/sciencecenter3.jpg"]
imagesPaths4 = ["./stitching_images/fourthSet/bookstore5.jpg","./stitching_images/fourthSet/bookstore6.jpg","./stitching_images/fourthSet/bookstore7.jpg"]
imagesPaths5 = ["./stitching_images/fifthSet/tdeck1.jpg","./stitching_images/fifthSet/tdeck2.jpg","./stitching_images/fifthSet/tdeck3.jpg"]
images = []

for path in imagesPaths3:
	image = cv2.imread(path)
	images.append(image)

# stitcher=cv2.Stitcher.create()
print(len(images))
stitcher = cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)

if status == 0:
	print("stiching is successful")
	cv2.imshow("Stitched", stitched)
	cv2.imwrite("stichedImage.png", stitched)
	cv2.waitKey(0)
else:
	print("[INFO] image stitching failed ({})".format(status))

