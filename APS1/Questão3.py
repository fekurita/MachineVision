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
    #transformar para uma matriz inteira de 16 bits
    frame_gray_new_16 =frame_gray_new.astype(np.int16)
    #Cria matriz base de comparação
    if frame_atual == 1:
        frame_base =frame_gray_new_16
    #Calcula diferença entre frames
    Diferenca= abs(frame_base-frame_gray_new)
    #Cria a matriz de diferenças
    frame_show =np.where(Diferenca<30,0,255)

    cv2.imshow("Video", frame_show.astype(np.uint8))
    #frame_gray_old = frame_gray_new_16
    frame_atual += 1
    # Press “q” on keyboard to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break