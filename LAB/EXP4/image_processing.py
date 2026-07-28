import cv2
import numpy as np

# Read the image
image = cv2.imread("flower.png")   # Replace with your image name

# Check if the image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Create a kernel
kernel = np.ones((5, 5), np.uint8)

# Apply Dilation
dilated = cv2.dilate(image, kernel, iterations=1)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Dilated Image", dilated)

# Save the dilated image
cv2.imwrite("dilated_flower.png", dilated)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()