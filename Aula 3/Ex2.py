import cv2
import matplotlib.pyplot as plt
img = cv2.imread("Figuras/Fig2a.bmp", cv2.IMREAD_COLOR)
#cv2.IMREAD_COLOR: Alternatively, we can pass integer value 1 for this flag.
#cv2.IMREAD_GRAYSCALE: Alternatively, we can pass integer value 0 for this flag
#caso nao seja indicado nada, o flag default eh cv2.IMREAD_COLOR
print("\nFig Shape = ", img.shape)
print("Data type of the ndarray = ", img.dtype)
print("\nDados do Pixel(0,0) no formato BGR")
print(img[0,0])
plt.imshow(img)
plt.show()