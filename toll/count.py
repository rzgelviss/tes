import os
import sys
import xml.etree.ElementTree as ET

path = r'D:\PythonProject\SSD-Tensorflow-master\img_from_camera\img-PascalVOC-export\Annotations'
# path = './xml'
xml_list = os.listdir(path)
# print(xml_list)
sum = []
for i in xml_list:
    filename = os.path.join(path, i)
    # print(filename)
    tree = ET.parse(filename)
    # print(tree)
    root = tree.getroot()
    # print(root)
    size = root.find('size')
    # print(size.find('width').text)
    for obj in root.findall('object'):
        label = obj.find('name').text
        # print(label)
        sum.append(label)
print(sum)
print(len(sum))
