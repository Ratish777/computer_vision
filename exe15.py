
import cv2
import numpy as np

img = cv2.imread(r'C:/Users/harsh/OneDrive/Desktop/computer vision/cv.jpg')
if img is None:
    print("Image not found!")
    exit()

rows, cols = img.shape[:2]
src = np.float32([[100, 100], [400, 100], [100, 400], [400, 400]])
dst = np.float32([[80, 120], [410, 90], [120, 450], [430, 440]])
H, _ = cv2.findHomography(src, dst, method=0)
output = cv2.warpPerspective(img, H, (cols, rows))

cv2.imshow("DLT Transform", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
