import cv2

# Read original image
image = cv2.imread("C:/Users/harsh/OneDrive/Desktop/computer vision/cv.jpg")

# Resize to bigger (e.g. 2x)
bigger = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

# Resize to smaller (e.g. 0.5x)
smaller = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Show results
cv2.imshow('Original', image)
cv2.imshow('Bigger', bigger)
cv2.imshow('Smaller', smaller)
cv2.waitKey(0)
cv2.destroyAllWindows()
