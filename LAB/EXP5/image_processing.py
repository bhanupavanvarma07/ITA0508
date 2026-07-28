import cv2
import numpy as np

# Read the image
image = cv2.imread("mickey.png")   # Replace with your image name

# Check if the image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Create a kernel
kernel = np.ones((5, 5), np.uint8)

# Apply Erosion
eroded = cv2.erode(image, kernel, iterations=1)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", eroded)

# Save the eroded image
cv2.imwrite("eroded_mickey.png", eroded)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()