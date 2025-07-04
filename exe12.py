import cv2
import numpy as np

img = cv2.imread(r'C:/Users/harsh/OneDrive/Desktop/computer vision/cv.jpg')
if img is None:
    print("Image not found!")
    exit()

rows, cols = img.shape[:2]
pts1 = np.float32([[50, 50], [cols - 50, 50], [50, rows - 50], [cols - 50, rows - 50]])
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
M = cv2.getPerspectiveTransform(pts1, pts2)
output = cv2.warpPerspective(img, M, (300, 300))

cv2.imshow("Perspective Transform", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
