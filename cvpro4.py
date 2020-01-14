import numpy as np
import cv2
img = cv2.imread( r"C:\Users\Chanchal\Desktop\watch.jfif" , cv2.IMREAD_COLOR)

px = img[55,55]
img[55,55] = [255,255,255]
print(px)
#Region Of Image
roi = img[100:150,100:150] = [255,255,255]
#print(roi)
watch_face = img[37:100,67:103]
#redefining region of image 111-37,194-107
img[0:63,0:36] = watch_face
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
