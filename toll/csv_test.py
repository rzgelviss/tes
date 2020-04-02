import os
import pandas as pd
import numpy as np
import glob
import cv2
from skimage import io
import re


i = 0
path = r'D:\PythonProject\SSD-Tensorflow-master\google_data\img'

img_list = glob.glob(path + '/*.jpg')
print(img_list)
img_list = [i.split('\\')[-1] for i in img_list]
print(img_list)
with open('./label2.csv', 'w') as file:
    file.write('filename,width,height,class,xmin,ymin,xmax,ymax\n')
    label_list = []
    with open('./class-descriptions.csv', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            # print(line)
            r = re.findall(r'(.*boat.*)', line, re.I)
            if r != []:
                # print(r)
                label = r[0].split(',')[0]
                label_list.append(label)
    with open('./train-annotations-bbox.csv', 'r') as f:
        data = f.readlines()
        # cv2.namedWindow('tes', cv2.WINDOW_NORMAL)
        for line in data:
            line = line.split(',')
            img_name = line[0] + '.jpg'
            if (img_name in img_list):
                if line[2] in label_list:
                    # print(line)
                    # print(img_name)

                    i += 1
                    print(i)
                    img_path = os.path.join(path, img_name)
                    # print(img_path)
                    img = io.imread(img_path)
                    # print(img.shape)
                    if len(img.shape) == 3:
                        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                        # print(img.shape)
                        h = img.shape[0]
                        w = img.shape[1]
                        cls = 'ship'
                        xmin = int(float(line[4]) * w)
                        xmax = int(float(line[5]) * w)
                        ymin = int(float(line[6]) * h)
                        ymax = int(float(line[7]) * h)
                        # print(str(w))
                        # print(str(int(xmin)))

                        # color = (0, 255, 255)
                        # cv2.rectangle(img, (xmin, ymin), (xmax, ymax), color, 2)
                        # cv2.imshow('tes', img)
                        # cv2.waitKey(200)
                        content = img_path + ',' + str(w) + ',' + str(h) + ',' + cls + ',' + str(xmin) + ',' + str(xmax) + ',' + str(ymin) + ',' + str(ymax) + '\n'
                        file.write(content)
                        # cv2.imshow('test', img)
                        # cv2.waitKey(1000)

