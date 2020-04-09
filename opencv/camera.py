import cv2
import time
camera_type = [0, 1]
chose_camera = camera_type[0]
capture = cv2.VideoCapture(chose_camera)
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, 5000)
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 5000)
print('opencamara')
#获取捕获的分辨率

capture.set(cv2.CAP_PROP_FRAME_WIDTH, 500)#;//宽度 
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)#;//高度
# capture.set(cv2.CAP_PROP_FPS, 30)#;//帧率 帧/秒
# capture.set(cv2.CAP_PROP_BRIGHTNESS, 1)#;//亮度 1
# capture.set(cv2.CAP_PROP_CONTRAST,40)#;//对比度 40
# capture.set(cv2.CAP_PROP_SATURATION, 50)#;//饱和度 50
# capture.set(cv2.CAP_PROP_HUE, 50)#;//色调 50
# capture.set(cv2.CAP_PROP_EXPOSURE, 50)#;//曝光 50
#获取摄像头参数
# capture.get(cv2.CAP_PROP_FRAME_WIDTH)
# capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
# capture.get(cv2.CAP_PROP_FPS)
# capture.get(cv2.CAP_PROP_BRIGHTNESS)
# capture.get(cv2.CAP_PROP_CONTRAST)
# capture.get(cv2.CAP_PROP_SATURATION)
# capture.get(cv2.CAP_PROP_HUE)
# capture.get(cv2.CAP_PROP_EXPOSURE)


i=0
cv2.namedWindow("test", cv2.WINDOW_NORMAL)
cv2.resizeWindow('test', 640, 480)
size =(int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
       int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(size)
print(capture.get(cv2.CAP_PROP_FPS))


#设置要保存的视频的编码，分辨率和帧率
video= cv2.VideoWriter(
    "time_lapse.avi",
    cv2.VideoWriter_fourcc('M', 'P', '4', '2'),
    24, # 输出文件帧率
    size
)
# 对于低画质的摄像头，前面的帧可能不稳定，略过
# for i in range(42):
#     capture.read()
# try:
#     for i in range(50):
#         _, frame = capture.read()
#         video.write(frame)
#         time.sleep(1)
# except KeyboardInterrupt:
#     print('stopped')
# video.release()



#
# import sys
# print(sys.argv)
#
while capture.isOpened():
    # print('in')
    ret, frame = capture.read()
    if i % 20 == 0:

        # print(frame)
        kk = cv2.waitKey(1)  # 每帧数据延时1ms

        cv2.circle(frame, (300, 100), 50, (0, 255, 0), -1)


        print(frame.shape)
    cv2.imshow("test", frame)
    i += 1

    # if cv2.waitKey(1) &0XFF == ord('s'):
    #     print(str(i) + '.jpg')
    #     cv2.imwrite(str(i) + '.jpg', frame)
    #     print('ok')

    if cv2.waitKey(30) == 27:
        break

capture.release()
cv2.destroyAllWindows()