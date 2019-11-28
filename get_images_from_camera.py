
import numpy as np  # 数据处理的库 Numpy
import cv2          # 图像处理的库 OpenCv

import os           # 读写文件
import shutil       # 读写文件
import time

# OpenCv 调用摄像头 use camera
cap = cv2.VideoCapture(r'D:\PythonProject\data\视频\视频/IMG_2345.MOV')

# 设置视频参数 set camera
cap.set(3, 480)


cnt_ss = 0

# 存储的文件夹 the folder to save faces
current_face_dir = ""

# 保存 images 的路径 the directory to save images of faces
path_photos_from_camera = "img_from_camera/"


# 新建保存图像文件
# mkdir for saving photos and csv
def pre_work_mkdir():

    # 新建文件夹 / make folders to save faces images and csv
    if os.path.isdir(path_photos_from_camera):
        pass
    else:
        os.mkdir(path_photos_from_camera)


pre_work_mkdir()

i = 0
while cap.isOpened():
    flag, img_rd = cap.read()
    # print(img_rd.shape)
    # It should be 480 height * 640 width

    kk = cv2.waitKey(1)

    current_face_dir = path_photos_from_camera
    # os.makedirs(current_face_dir)

    # 按下 's' 保存摄像头中的人脸到本地 / press 's' to save faces into local images
    if kk == ord('s'):
        # 检查有没有先按'n'新建文件夹 / check if you have pressed 'n'
        i += 1
        cv2.imwrite(current_face_dir + "img_face_" + str(int(time.time())) + '_' + str(i) + ".jpg", img_rd)
        print("写入本地 / Save into：", str(current_face_dir) + "/img_face_" + str(cnt_ss) + ".jpg")

    # 按下 'q' 键退出 / press 'q' to exit
    if kk == ord('q'):
        break

    # 如果需要摄像头窗口大小可调 / uncomment this line if you want the camera window is resizeable
    # cv2.namedWindow("camera", 0)

    cv2.imshow("camera", img_rd)

# 释放摄像头 / release camera
cap.release()
cv2.destroyAllWindows()
