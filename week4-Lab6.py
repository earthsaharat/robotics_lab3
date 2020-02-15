import cv2
import numpy as np

img = cv2.imread("container.jpg", cv2.IMREAD_COLOR)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret,thresh1 = cv2.threshold(img_gray,200,255,cv2.THRESH_BINARY)

cv2.imshow('original',img)
cv2.imshow('threshold',thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()