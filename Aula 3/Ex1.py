import cv2
import matplotlib.pyplot as plt
img = cv2.imread("Figuras/Fig1a.bmp", cv2.IMREAD_GRAYSCALE)
if img is None:
    print("File not found. Bye!")
    exit(0)
print("\nData type = ", type(img))
print("Data type of the ndarray = ", img.dtype)
print("Fig Shape = ", img.shape)
print("\nDados da figura")
print(img)
# Opcao1: mostrando figura a partir do próprio OpenCV
cv2.imshow('Fig', img )
#aguarde pressionar um tecla (ou algum tempo em mseg)
cv2.waitKey(0)
# Opcao2: mostrando figura a partir do plt (usar cmap='gray' caso imagemGRAYSCALE)
plt.imshow(img, cmap='gray')
plt.show()
