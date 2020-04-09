import cv2
import numpy as np


# img = cv2.imread(r'./demo03.jpg', 3)
img = cv2.imread(r'./3.png', 3)
# lower_y = np.array([26, 43, 46])
# upper_y = np.array([34, 255, 255])
lower_y = np.array([0, 72, 178])
upper_y = np.array([181, 186, 252])

color_y = (0, 255, 255)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask_y = cv2.inRange(hsv, lower_y, upper_y)
contours, hierarchy = cv2.findContours(mask_y, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

area_box = []
rect_y = []
R = []

crop = 0
height = 15
perc = 8
x = 0
print(mask_y.shape)
y = int(mask_y.shape[0] * crop / 100)
w = int(mask_y.shape[1])
h = int(mask_y.shape[0] * height / 100)
img_cropped = mask_y[y: y + h, x: x + w]

print(cv2.countNonZero(mask_y))
print(img_cropped.size * perc / 100)

for contour in contours:
    # if cv2.contourArea(contour) > 4500 and cv2.contourArea(contour) < 12000:
    if cv2.contourArea(contour) > 4000:
        # print(contour)
        # cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)
        area_box.append(contour)
        rect = cv2.minAreaRect(contour)
        rect_y.append(rect)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        cv2.drawContours(img, [box], -1, color_y, 2)
        cv2.putText(img, 'y', (int(rect[0][0]), int(rect[0][1])), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)




cv2.namedWindow('win', cv2.WINDOW_NORMAL)
cv2.imshow('win', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
