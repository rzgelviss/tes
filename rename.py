# coding=gbk
import os
import re
import sys


# import sys, io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') # Change default encoding to utf8
fileList = os.listdir(r"D:\PythonProject\SSD-Tensorflow-master\tfrecords_7")
# ������ļ����а������ļ�����
print("�޸�ǰ��" + str(fileList))
# �õ����̵�ǰ����Ŀ¼
currentpath = os.getcwd()
# ����ǰ����Ŀ¼�޸�Ϊ���޸��ļ��е�λ��
os.chdir(r"D:\PythonProject\SSD-Tensorflow-master\tfrecords_7")
# ���Ʊ���
num = 535
# �����ļ����������ļ�
for fileName in fileList:
    # ƥ���ļ���������ʽ
    pat = ".+\.(tfrecord)"
    # ����ƥ��
    pattern = re.findall(pat, fileName)
    # �ļ���������
    os.rename(fileName, ('voc_2007_train_0' + str(num) + '.' + pattern[0]))
    # �ı��ţ�������һ��
    num = num + 1
print("***************************************")
# �Ļس�������ǰ�Ĺ���Ŀ¼
os.chdir(currentpath)
# ˢ��
sys.stdin.flush()
# print("�޸ĺ�" + str(os.listdir(r"./neteasy_playlist_data3"))[1])

