kernel = np.array([[0,1,0],[1,-4,1],[0,1,0]])
lap = cv2.filter2D(img, -1, kernel)
sharpened = cv2.subtract(img, lap)
cv2.imshow("22. Laplacian Positive Center", sharpened); cv2.waitKey(0); cv2.destroyAllWindows()
