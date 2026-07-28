import cv2

# Read the image
image = cv2.imread("nature.png")    # Replace with your image name

# Check if the image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur to reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Detect edges using the Canny function
edges = cv2.Canny(blur, 100, 200)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Canny Edge Detection", edges)

# Save the edge-detected image
cv2.imwrite("canny_output.png", edges)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()