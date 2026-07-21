import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("sample.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Simulate improper sampling
small = cv2.resize(img, (100, 100))
blurred = cv2.resize(small, (img.shape[1], img.shape[0]))

# Better sampling
corrected = cv2.resize(small, (img.shape[1], img.shape[0]),
                       interpolation=cv2.INTER_CUBIC)

plt.figure(figsize=(10,4))

plt.subplot(1,3,1)
plt.imshow(img)
plt.title("Original")

plt.subplot(1,3,2)
plt.imshow(blurred)
plt.title("Improper Sampling")

plt.subplot(1,3,3)
plt.imshow(corrected)
plt.title("Corrected")

plt.show()