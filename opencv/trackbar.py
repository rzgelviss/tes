import cv2
import numpy as np


# img = cv2.imread('demo03.jpg')
img = cv2.imread('1.png', 3)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def nothing(x):
    pass


cv2.namedWindow('winName', cv2.WINDOW_NORMAL)
cv2.resizeWindow('winName', 640, 480)
# cv2.imshow('winName', img)
cv2.createTrackbar('LowerbH', 'winName', 0, 255, nothing)
cv2.createTrackbar('LowerbS', 'winName', 0, 255, nothing)
cv2.createTrackbar('LowerbV', 'winName', 0, 255, nothing)
cv2.createTrackbar('UpperbH', 'winName', 0, 255, nothing)
cv2.createTrackbar('UpperbS', 'winName', 0, 255, nothing)
cv2.createTrackbar('UpperbV', 'winName', 0, 255, nothing)
while True:
    lowerbH = cv2.getTrackbarPos('LowerbH', 'winName')
    lowerbS = cv2.getTrackbarPos('LowerbS', 'winName')
    lowerbV = cv2.getTrackbarPos('LowerbV', 'winName')
    upperbH = cv2.getTrackbarPos('UpperbH', 'winName')
    upperbS = cv2.getTrackbarPos('UpperbS', 'winName')
    upperbV = cv2.getTrackbarPos('UpperbV', 'winName')
    # print(np.array([lowerbH, lowerbS, lowerbV]))
    # 得到目标颜色的二值图像，用作cv.bitwise_and()的掩膜
    img_target = cv2.inRange(img, (lowerbH, lowerbS, lowerbV), (upperbH, upperbS, upperbV))
    #输入图像与输入图像在掩膜条件下按位与，得到掩膜范围内的原图像
    img_specifiedColor = cv2.bitwise_and(img, img, mask=img_target)
    cv2.namedWindow('win', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('win', 640, 480)
    cv2.imshow('win', img_specifiedColor)
    # cv2.imshow('winName', img)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()