import cv2
import numpy as np

img = cv2.imread(r'C:/Users/harsh/OneDrive/Desktop/computer vision/cv.jpg')
if img is None:
    print("Image not found!")
    exit()

kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

sharpened = cv2.filter2D(img, -1, kernel)

cv2.imshow("Laplacian Sharpening", sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
