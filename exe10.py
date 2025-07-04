import cv2
import numpy as np

image = cv2.imread(r'C:/Users/harsh/OneDrive/Desktop/computer vision/cv.jpg')

M = np.float32([[1, 0, 100], [0, 1, 50]])
moved = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))

cv2.imwrite('moved_small.jpg', moved)
print("Moved image saved as 'moved_small.jpg'")
