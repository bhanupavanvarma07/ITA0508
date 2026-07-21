import cv2
import matplotlib.pyplot as plt

img = cv2.imread("sample.jpg",0)

# 8-bit image
bit8 = img

# Reduce to 4-bit
bit4 = (img//16)*16

plt.subplot(1,2,1)
plt.imshow(bit8,cmap='gray')
plt.title("8-bit")

plt.subplot(1,2,2)
plt.imshow(bit4,cmap='gray')
plt.title("4-bit Quantization")

plt.show()