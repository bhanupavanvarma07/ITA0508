import cv2

# Read the image
image = cv2.imread("house.png")   # Replace with your image name

# Check if the image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Apply Gaussian Blur
blur = cv2.GaussianBlur(image, (15, 15), 0)

# Display the original image
cv2.imshow("Original Image", image)

# Display the blurred image
cv2.imshow("Gaussian Blur Image", blur)

# Save the blurred image
cv2.imwrite("blur_house.png", blur)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()