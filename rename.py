# coding=gbk
import os
import re
import sys


# import sys, io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') # Change default encoding to utf8
fileList = os.listdir(r"D:\PythonProject\SSD-Tensorflow-master\tfrecords_7")
# 输出此文件夹中包含的文件名称
print("修改前：" + str(fileList))
# 得到进程当前工作目录
currentpath = os.getcwd()
# 将当前工作目录修改为待修改文件夹的位置
os.chdir(r"D:\PythonProject\SSD-Tensorflow-master\tfrecords_7")
# 名称变量
num = 535
# 遍历文件夹中所有文件
for fileName in fileList:
    # 匹配文件名正则表达式
    pat = ".+\.(tfrecord)"
    # 进行匹配
    pattern = re.findall(pat, fileName)
    # 文件重新命名
    os.rename(fileName, ('voc_2007_train_0' + str(num) + '.' + pattern[0]))
    # 改变编号，继续下一项
    num = num + 1
print("***************************************")
# 改回程序运行前的工作目录
os.chdir(currentpath)
# 刷新
sys.stdin.flush()
# print("修改后：" + str(os.listdir(r"./neteasy_playlist_data3"))[1])

