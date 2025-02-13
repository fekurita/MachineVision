import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("Figuras/Fig2b.bmp", cv2.IMREAD_COLOR)

(h,w,c) = img.shape
print("height =",h)
print("Width =",w)

img_bin = np.zeros((h,w),dtype = "uint8")

for i in range(h):
    for j in range (w):
       img_bin[i,j] = img[i,j,0]*0.07+img[i,j,1]*0.72+img[i,j,2]*0.21 
print("\nDados da figura")
print(img)
# Opcao2: mostrando figura a partir do plt (usar cmap='gray' caso imagemGRAYSCALE)
plt.imshow(img_bin, cmap='gray')
plt.show()