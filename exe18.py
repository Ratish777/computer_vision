import cv2
import numpy as np

img = cv2.imread(r'C:/Users/harsh/OneDrive/Desktop/computer vision/cv.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)

cv2.imshow("Sobel Y", cv2.convertScaleAbs(sobely))
cv2.waitKey(0)
cv2.destroyAllWindows()
