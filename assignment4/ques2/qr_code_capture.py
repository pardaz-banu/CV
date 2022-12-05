import glob
import cv2
import pandas as pd
import pathlib

def read_qr_code(img):
    detect = cv2.QRCodeDetector()
    value, points, straight_qrcode = detect.detectAndDecode(img)
    return value

# img = cv2.imread("business_card.jpeg")
# print(read_qr_code(img))