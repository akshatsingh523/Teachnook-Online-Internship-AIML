#2 creating a duplicate image
import cv2
img=cv2.imread('download.jpg')
cv2.imshow('IMAGE',img)
cv2.imwrite('download(1).jpg',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
