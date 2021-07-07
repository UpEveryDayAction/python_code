import cv2

img = cv2.imread("src/Lena.jpg",0)
"""
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
print(img_gray.shape)
"""
cv2.imshow("window_default", img)
cv2.namedWindow("window_resize", cv2.WINDOW_NORMAL)
#cv2.resizeWindow("window_resize",640,480)
cv2.resizeWindow("window_resize",320,240)
cv2.imshow("window_resize", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
