import cv2
camera_type = [0, 1]
chose_camera = camera_type[0]
capture = cv2.VideoCapture(chose_camera)
print('opencamara')
while capture.isOpened():
    # print('in')
    ret, frame = capture.read()
    # print(frame)
    kk = cv2.waitKey(2)  # 每帧数据延时1ms
    print(kk)
    cv2.namedWindow("test", cv2.WINDOW_NORMAL)
    cv2.circle(frame, (300, 100), 50, (0, 0, 255), -1)
    color = (0, 255, 0)
    Camera1_text = "Camera1 Detected"
    cv2.rectangle(frame, (1, 10), (frame.shape[1], frame.shape[0]), color, 2)
    cv2.putText(frame, Camera1_text, (30, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
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