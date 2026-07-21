import cv2

img = cv2.imread("sample.jpg")

# Create low-light image
low = cv2.convertScaleAbs(img, alpha=0.4, beta=-30)

# Brightness enhancement
enhanced = cv2.convertScaleAbs(low, alpha=2.0, beta=40)

cv2.imshow("Original", img)
cv2.imshow("Low Light", low)
cv2.imshow("Enhanced", enhanced)

cv2.waitKey(0)
cv2.destroyAllWindows()