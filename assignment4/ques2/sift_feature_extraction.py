import cv2

def sift_extract(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    # detect features from the image
    keypoints, descriptors = sift.detectAndCompute(img, None)
    # draw the detected key points
    sift_image = cv2.drawKeypoints(gray, keypoints, img)
    # show the image
    cv2.imshow('image', sift_image)
    # save the image
    cv2.imwrite("table-sift.jpg", sift_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()