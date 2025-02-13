import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("Figuras/Fig4.bmp", cv2.IMREAD_COLOR)

(h,w,c) = img.shape
print("height =",h)
print("Width =",w)

img_bin = np.zeros((h,w,c),dtype = "uint8")

for i in range(h):
    for j in range (w):
        if img[i,j,0] < 20 and img[i,j,1] < 20 and img[i,j,2]> 205:
            img_bin[i,j]=[0,75,150]
        else:
            img_bin[i,j] = img[i,j]
print("\nDados da figura")
print(img)
# Opcao2: mostrando figura a partir do plt (usar cmap='gray' caso imagemGRAYSCALE)
imgRGB = cv2.cvtColor(img_bin,cv2.COLOR_BGR2RGB)
plt.imshow(imgRGB)
plt.show()