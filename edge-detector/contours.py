import numpy as np
import cv2

image = cv2.imread('shl_1.jpg')
original = image.copy()
image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower = np.array([0, 0, 207], dtype="uint8")
upper = np.array([179, 255, 255], dtype="uint8")
mask = cv2.inRange(image, lower, upper)

# adjust this
ksize = (3, 3)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, ksize)
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=1)

cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]

area = 0
for c in cnts:
    area += cv2.contourArea(c)
    cv2.drawContours(original, [c], 0, (0, 0, 0), 2)

print(area)
cv2.imshow('mask', mask)
cv2.imshow('original', original)
cv2.imshow('opening', opening)
cv2.waitKey()
