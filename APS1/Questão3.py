import numpy as np
import cv2
# read video
cap = cv2.VideoCapture('Figuras_APS1/Video_APS1_3.avi')
num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Nro frames = ", num_frames)
frame_atual = 1
while (frame_atual < num_frames):
# leitura sequencia dos frames do video
    ret, frame = cap.read()
    frame_gray_new = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if frame_atual == 1:
        frame_gray_old =frame_gray_new
    frame_show =np.where(abs(frame_gray_old-frame_gray_new)<20,0,frame_gray_old)
    cv2.imshow("Video", frame_show)
    frame_gray_old = frame_gray_new
    frame_atual += 1
    # Press “q” on keyboard to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break