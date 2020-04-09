import cv2 as cv
import numpy as np
import os


def read_py(path):
    k = 0
    lis = os.listdir(path)
    for i in lis:
        file_path = os.path.join(path, i)
        if os.path.isdir(file_path):
            read_py(file_path)
        else:
            if i.endswith('.jpg'):
                print(file_path)
                img = cv.imread('file_path')
                cv.imwrite('./data/{}.jpg'.format(k), img)
                k += 1
                # print(file_path)


# img = cv.imread('./sample1.jpg')
# print(img.shape)
# img1 = img[130:160, 50:270, :3]
# print(img1)
# cv.imwrite('target1.jpg', img1)
#
#
#
# cv.namedWindow('show')
# cv.imshow('show', img1)
# cv.waitKey(0)

if __name__ == '__main__':
    path = './'
    # read_py(path)
    # import cv2
    # ss=1
    # # img = cv2.imread(r"./img/%d.jpg"%(ss), 3)
    # img = cv2.imread(r"./img/01.jpg", 3)
    # print(img)
    # cv2.imshow("test", img)
    # cv2.waitKey(2000)
    # import re
    # ca = re.findall(r"\d+", "ca=500")[0]
    # print(ca)

