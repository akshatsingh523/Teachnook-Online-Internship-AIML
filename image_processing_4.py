import cv2
img=cv2.imread('download.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('ORIGNAL NAME',img)
cv2.imshow('GRAY SCALE IMAGE',gray)
cv2.waitkey(0)
cv2.destroyAllWindows()
