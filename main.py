import cv2
import numpy as np

# red color
img = cv2.imread('frame1.png')
result = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_red = np.array([0, 30, 50])
upper_red = np.array([10, 255, 255])
mask = cv2.inRange(img, lower_red, upper_red)
result = cv2.bitwise_and(result, result, mask=mask)

#cv2.imshow('mask', mask)
cv2.imshow('result', result)
cv2.waitKey()
cv2.destroyAllWindows()

# blue color
img = cv2.imread('frame1.png')
result = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_blue = np.array([100,50,50])
upper_blue = np.array([130,255,255])
mask = cv2.inRange(img, lower_blue, upper_blue)
result = cv2.bitwise_and(result, result, mask=mask)

#cv2.imshow('mask', mask)
cv2.imshow('result', result)
cv2.waitKey()
cv2.destroyAllWindows()

