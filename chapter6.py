import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")

imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))

cv2.imshow('Image1',imgHor)
cv2.imshow('Image2',imgVer)


cv2.waitKey(0)