import cv2

# Read image
image = cv2.imread("tree.png")

# Check if image is loaded
if image is None:
    print("Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display images
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)

# Save grayscale image
cv2.imwrite("gray_tree.png", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()