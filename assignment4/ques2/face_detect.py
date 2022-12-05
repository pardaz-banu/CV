# OpenCV program to detect face in real time
# import libraries of python OpenCV
# where its functionality resides
import cv2
import matplotlib.pyplot as plt

def detect_face(img):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#img = cv2.imread("business_card.jpeg")
#print(img)
	# convert to gray scale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	# Detects faces of different sizes in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

		#eyes = eye_cascade.detectMultiScale(roi_gray)
        # for (ex,ey,ew,eh) in eyes:
		#     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)

	# Display an image in a window
    return img

	# Wait for Esc key to stop

# De-allocate any associated memory usage

