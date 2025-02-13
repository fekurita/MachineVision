import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("Figuras/Fig5.bmp", cv2.IMREAD_GRAYSCALE)

(h,w) = img.shape
print("height =",h)
print("Width =",w)

Black = 0

for i in range(h):
    for j in range (w):
        if img[i,j] <100:
            Black+=1

print((Black/(h*w))*100)
