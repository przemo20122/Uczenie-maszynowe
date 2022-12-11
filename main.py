import cv2
import numpy as np

cap = cv2.VideoCapture('one round kam4.mp4')
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output_video.mp4', fourcc, 30, (1920, 1080))
background_substraction = cv2.createBackgroundSubtractorMOG2()

while 1:
    st, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # lower mask red
    lower_red = np.array([0, 170, 50])
    upper_red = np.array([5, 255, 255])
    mask_red1 = cv2.inRange(img, lower_red, upper_red)

    # upper mask red
    lower_red = np.array([170, 150, 50])
    upper_red = np.array([180, 255, 255])
    mask_red2 = cv2.inRange(img, lower_red, upper_red)

    # mask blue
    lower_blue = np.array([100, 80, 2])
    upper_blue = np.array([129, 255, 255])
    mask_blue = cv2.inRange(img, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask=mask_red1 + mask_red2 + mask_blue)
    background_mask = background_substraction.apply(frame)
    out.write(cv2.copyTo(result, background_mask))
    # out.write(result)

cap.release()
cv2.waitKey()
cv2.destroyAllWindows()
