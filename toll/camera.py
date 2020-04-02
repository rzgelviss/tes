import cv2
camera_type = [0, 1]
chose_camera = camera_type[0]
# capture = cv2.VideoCapture('rtmp://192.168.1.41:1935/mylive/test')
capture = cv2.VideoCapture(0)
print('opencamara')
while capture.isOpened():
    # print('in')
    ret, frame = capture.read()
    # print(frame)
    kk = cv2.waitKey(2)  # 每帧数据延时1ms
    print(kk)
    cv2.namedWindow("test", cv2.WINDOW_NORMAL)
    cv2.circle(frame, (300, 100), 50, (0, 0, 255), -1)
    cv2.imshow("test",frame)

    # print('flage=1')
    #
    # print('over')

        # return Movement(frame)
        # pass
    #
    # else:
    #     pass
        # return 0
capture.release()
cv2.destroyAllWindows()