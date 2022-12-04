import cv2
import numpy as np

cap = cv2.VideoCapture('output_video.mp4')
fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output_video2.mp4', fourcc, 30, (1920, 1080))
fgbg = cv2.createBackgroundSubtractorMOG2()
fgbg = cv2.createBackgroundSubtractorKNN()


while 1:
    st, frame = cap.read()
    fgmask = fgbg.apply(frame)
    img = cv2.cvtColor(fgmask, cv2.COLOR_GRAY2BGR)
    cv2.imshow('FG Mask', fgmask)
    cv2.imshow('img', img)
    out.write(img)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    #out.write(fgmask)


cap.release()
cv2.waitKey()
cv2.destroyAllWindows()