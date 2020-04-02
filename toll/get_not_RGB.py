# encoding:utf-8
from PIL import Image
import os
import matplotlib.pyplot as plt


def get_not_rgb_images(rootdir):
    list = os.listdir(rootdir)
    l = len(list)
    count = 0
    for i in range(0, len(list)):
        filename = os.path.join(rootdir, list[i])
        # print(filename)
        if os.path.isfile(filename):
            img = Image.open(filename)
            pixels = img.getpixel((0, 0))

            if type(pixels) == int:
                print('单通道:' + filename)
                count += 1
                print('The ', i, 'st pic:', count, '/', l, '\r')
                # img = Image.open(imgName)
                img = img.convert('RGB')
                img.save(filename)

            elif type(pixels) == tuple:
                if len(pixels) != 3:
                    print('非RGB的多通道:' + filename)
                    count += 1
                    print('The ', i, 'st pic:', count, '/', l, '\r')
                    img = img.convert('RGB')
                    img.save(filename)
        else:
            get_not_rgb_images(filename)


if __name__ == '__main__':
    # rootdir = r'D:\PythonProject\SSD-Tensorflow-master\img_from_camera\img-PascalVOC-export\JPEGImages'  # 您图片所在的文件夹
    rootdir = './demo'
    get_not_rgb_images(rootdir)
