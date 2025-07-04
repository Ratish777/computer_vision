import cv2, numpy as np
img = cv2.imread(r'C:/Users/harsh/OneDrive/Desktop/computer vision/cv.jpg')
kernel = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])
output = cv2.filter2D(img, -1, kernel)
cv2.imshow("21. Diagonal Laplacian", output); cv2.waitKey(0); cv2.destroyAllWindows()
