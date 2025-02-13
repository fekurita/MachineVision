import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread("Figuras/Fig1b.bmp", cv2.IMREAD_GRAYSCALE)

(h,w) = img.shape
print("height =",h)
print("Width =",w)

img_bin = np.zeros((h,w),dtype = "uint8")

for i in range(h):
    for j in range (w):
        if img[i,j]>127:
            img_bin[i,j]=255
print("\nDados da figura")
print(img)
# Opcao2: mostrando figura a partir do plt (usar cmap='gray' caso imagemGRAYSCALE)
plt.imshow(img_bin, cmap='gray')
plt.show()