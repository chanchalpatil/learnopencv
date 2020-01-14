import numpy as np
import cv2
#img1 = cv2.imread( r"C:\Users\Chanchal\Desktop\a1.jpg")
#img2 = cv2.imread( r"C:\Users\Chanchal\Desktop\a2.jpg")
#add = img1+img2
#add = cv2.add(img1,img2)
#weighted = cv2.addWeighted(img1,0.6,img2,0.4,0)
#cv2.imshow('weighted',weighted)
img1 = cv2.imread( r"C:\Users\Chanchal\Desktop\a1.jpg")
img2 = cv2.imread( r"C:\Users\Chanchal\Desktop\watch.jfif")

rows,cols,channels =img2.shape
roi = img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img2gray, 220,255,cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask= mask_inv)
img2_fg = cv2.bitwise_and(img2,img2,mask=mask)

dat = cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dat
cv2.imshow('res',img1)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img2_fg',img2_fg)
cv2.imshow('dat',dat)
#cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
