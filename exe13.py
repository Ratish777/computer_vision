import cv2
import numpy as np

pts1 = np.float32([[100, 100], [500, 100], [100, 400], [500, 400]])
pts2 = np.float32([[0, 0], [400, 0], [0, 400], [400, 400]])
M = cv2.getPerspectiveTransform(pts1, pts2)

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    transformed = cv2.warpPerspective(frame, M, (400, 400))
    cv2.imshow("Perspective on Video", transformed)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
