import cv2

img = cv2.imread(r'C:/Users/harsh/OneDrive/Desktop/computer vision/cv.jpg')
if img is None:
    print("Image not found!")
    exit()

edges = cv2.Canny(img, 100, 200)

cv2.imshow("Canny Edge Detection", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
