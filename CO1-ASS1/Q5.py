import cv2

img = cv2.imread("sample.jpg")

# Add Gaussian Noise
noise = cv2.randn(img.copy(), (0,0,0), (30,30,30))
noisy = cv2.add(img, noise)

# Remove noise
filtered = cv2.GaussianBlur(noisy,(5,5),0)

cv2.imshow("Original", img)
cv2.imshow("Noisy", noisy)
cv2.imshow("Filtered", filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()