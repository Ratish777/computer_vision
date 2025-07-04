import cv2

image = cv2.imread(r'C:/Users/harsh/OneDrive/Desktop/computer vision/cv.jpg')

if image is None:
    print("Image not found.")
    exit()

clockwise = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
counter_clockwise = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite('rotated_clockwise.jpg', clockwise)
cv2.imwrite('rotated_counterclockwise.jpg', counter_clockwise)

print("Rotated images saved as 'rotated_clockwise.jpg' and 'rotated_counterclockwise.jpg'")
