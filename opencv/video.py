import cv2

cap = cv2.VideoCapture()
cap.open('Safety_Full_Hat_and_Vest.mp4')
# n_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# print(n_frames)
print(cap.get(cv2.CAP_PROP_FPS))
cv2.namedWindow('video')

# for i in range(n_frames):
#     ret, frame = cap.read()
#     cv2.imshow('video', frame)
#     if cv2.waitKey(1) == 27:
#         break
while cap.isOpened:
    ret, frame = cap.read()
    cv2.imshow('video', frame)
    if cv2.waitKey(30) == 27:
        break