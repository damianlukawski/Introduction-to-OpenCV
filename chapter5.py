import cv2
import numpy as np

img = cv2.imread("Resources/cards.jpg")

width, height = 250,350
pts1 = np.float32([[111,219],[287,188],[154,484],[324,440]])
pts2 = np.float32([[0,0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width,height))

print(matrix)

cv2.imshow('Image2',img)
cv2.imshow('Image',imgOutput)

cv2.waitKey(0)