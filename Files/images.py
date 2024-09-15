import cv2

# Load the first image
img1 = cv2.imread('../Images/img1.jpg')

# Load the second image
img2 = cv2.imread('../Images/img2.jpg')

# Display the first image in a window
cv2.imshow('First Image', img1)

# Display the second image in a window
cv2.imshow('Second Image', img2)

# Wait for the user to press any key to close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
