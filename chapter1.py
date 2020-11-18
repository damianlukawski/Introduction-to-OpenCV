import cv2
print("Package Imported")


'''
#reading and playing image
img = cv2.imread('resources/lena.png')
cv2.imshow("Output", img)
cv2.waitKey(0)

#reading and playing video
cap = cv2.VideoCapture('resources/test_video.mp4')
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
'''

#reading and playing webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break