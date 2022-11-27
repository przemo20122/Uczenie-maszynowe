import cv2
import numpy as np

cap = cv2.VideoCapture('one round kam4.mp4')
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output_video.mp4', fourcc, 30, (1920, 1080))

while(1):
    st, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 170, 80])
    upper = np.array([140, 255, 255])
    mask = cv2.inRange(img, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    out.write(result)


cap.release()
cv2.waitKey()
cv2.destroyAllWindows()


# img = cv2.imread('frame1.png')
# result = img.copy()
# img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# lower_blue = np.array([100,50,50])
# upper_blue = np.array([130,255,255])
# mask = cv2.inRange(img, lower_blue, upper_blue)
# result = cv2.bitwise_and(result, result, mask=mask)
# cv2.imshow('result', result)

