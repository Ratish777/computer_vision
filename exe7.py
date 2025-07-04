import cv2
import time

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

print("Press 's' for slow motion, 'f' for fast motion, 'n' for normal, and 'q' to quit")

delay = 30

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Can't receive frame. Exiting...")
        break

    cv2.imshow('Webcam Video', frame)

    key = cv2.waitKey(delay) & 0xFF

    if key == ord('q'):  
        break
    elif key == ord('s'):  
        delay = 100
    elif key == ord('f'):  
        delay = 1
    elif key == ord('n'):
        delay = 30


cap.release()
cv2.destroyAllWindows()
