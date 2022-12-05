import face_detect
import qr_code_capture
import cv2
import matplotlib.pyplot as plt
import sift_feature_extraction
import edge_detection

img = cv2.imread("business_card1.jpeg")

face_det = face_detect.detect_face(img) #face detection

img_qr_face = qr_code_capture.read_qr_code(face_det) #extracting qr code from the image

cv2.imshow("Result",face_detect.detect_face(img))

sift_feature_extraction.sift_extract(face_det) #applying SIFT feature extraction

#applying edge detection to the business card
edge_detection.edge(img)

cv2.waitKey()