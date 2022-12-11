import cv2
import numpy as np

cap = cv2.VideoCapture('output_video.mp4')
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output_video2.mp4', fourcc, 30, (1920, 1080))
background_substraction = cv2.createBackgroundSubtractorMOG2()
# background_substraction = cv2.createBackgroundSubtractorKNN()

while 1:
    st, frame = cap.read()
    background_mask = background_substraction.apply(frame)
    result = cv2.cvtColor(background_mask, cv2.COLOR_GRAY2BGR)
    out.write(result)
    # if cv2.waitKey(30) & 0xFF == ord('q'):
    #    break

cap.release()
out.release()
