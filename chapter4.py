import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
print(img.shape)

#convert a part of image to blue
#img[100:400,20:100]=255,0,0

#cv2.line(image, starting coord, ending coord, color, width)
cv2.line(img, (100,100), (300,300), (0,255,0), 3)
cv2.rectangle(img, (50,400), (200, 450), (255,0,0), 2)
#cv2.rectangle(img, (400,400), (450, 450), (255,0,0), cv2.FILLED)
cv2.putText(img, 'Openenene',(300,300), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255,0,0),1)
cv2.imshow('s',img)

cv2.waitKey(0)
