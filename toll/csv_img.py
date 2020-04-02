import pandas as pd
from skimage import io
import cv2
import glob
import re
import requests


label_list = []
with open('./class-descriptions.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        # print(line)
        r = re.findall(r'(.*thermal mug.*)', line, re.I)
        if r != []:
            # print(r)

            label = r[0].split(',')[0]
            label_list.append(label)
print(label_list[:10])
df_img = pd.read_csv('./train-annotations-bbox.csv')
# print(df_img)
for label in label_list:
    try:
        print(label)
        img_name = df_img[df_img['LabelName'] == label]
        # print(img_name)
        img_list = list(img_name['ImageID'])
        print(len(img_list))
        df_url = pd.read_csv('./train-images-boxable.csv', sep=',')
        # print(df_url)
        img_list = list(set(img_list))
        down = []
        for i in glob.glob(r'D:\PythonProject\SSD-Tensorflow-master\google_data/tea/' + '*.jpg'):
            # print(i)
            down.append(i.split('\\')[-1].split('.')[0])
            img_list.remove(i.split('\\')[-1].split('.')[0])
        print(set(img_list))
        print(len(set(img_list)))
        i = 0
        for img in set(img_list):
            img = img + '.jpg'
            # print(img)
            # print(df_url[df_url['image_name'] == img])
            img_url = list(df_url[df_url['image_name'] == img]['image_url'])
            print(img_url[0])
            # try:
            #     img = io.imread(img_url[0])
            #     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            #     cv2.imwrite(img_url[0].split('/')[-1], img)
            #     print(i)
            #     i += 1
            # except Exception as e:
            #     print(e)
            try:
                img = requests.get(img_url[0], timeout=10, stream=True).raw.read()
                with open('./tea/' + img_url[0].split('/')[-1], 'wb') as file:
                    file.write(img)
                    print(i)
                    i += 1
                # time.sleep(1.5)
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
#



