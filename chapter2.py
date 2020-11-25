import cv2
import numpy as np


img = cv2.imread('resources/lena.png')
kernel = np.ones((5,5), np.uint8)

#convert to gray and add blur
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(img, 150,200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations = 1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.imshow("Canny Image", imgCanny)
cv2.waitKey(0)
