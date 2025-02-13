import cv2
import matplotlib.pyplot as plt
img = cv2.imread("Figuras/Fig3.bmp")
[B,G,R] = cv2.split(img)
plt.figure("RED")
plt.imshow(R, cmap='gray')
plt.figure("GREEN")
plt.imshow(G, cmap='gray')
plt.figure("BLUE")
plt.imshow(B, cmap='gray')
plt.show()