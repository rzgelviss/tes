# coding=gbk
import os
import re
import sys

# �޸ĺ����ֲ������ǰ��ͻ
# import sys, io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') # Change default encoding to utf8
fileList = os.listdir(r"D:\PythonProject\bottle_detect\opencv_haar_training-master\pos")
# ������ļ����а������ļ�����
print(fileList)
print("�޸�ǰ��" + str(fileList))
# �õ����̵�ǰ����Ŀ¼
currentpath = os.getcwd()
# ����ǰ����Ŀ¼�޸�Ϊ���޸��ļ��е�λ��
os.chdir(r"D:\PythonProject\bottle_detect\opencv_haar_training-master\pos")
# ���Ʊ���
num = 0
# �����ļ����������ļ�
for fileName in fileList:
    # ƥ���ļ���������ʽ
    print(fileName)
    pat = ".+\.(jpg)"
    # ����ƥ��
    pattern = re.findall(pat, fileName)
    # �ļ���������
    os.rename(fileName, (str(num) + '.' + pattern[0]))
    # �ı��ţ�������һ��
    num = num + 1
print("***************************************")
# �Ļس�������ǰ�Ĺ���Ŀ¼
os.chdir(currentpath)
# ˢ��
sys.stdin.flush()
# print("�޸ĺ�" + str(os.listdir(r"./neteasy_playlist_data3"))[1])

