import re
import os
import xml.etree.ElementTree as ET

#myself dataset path
annotation_folder = r'D:\PythonProject\SSD-Tensorflow-master\img_from_camera\img-PascalVOC-export\Annotations'
# annotation_folder = './xm'
list = os.listdir(annotation_folder)

def file_name(file_dir):
	L = []
	for root, dirs, files in os.walk(file_dir):
		for file in files:
			if os.path.splitext(file)[1] == '.xml':
				L.append(os.path.join(root, file))
	return L

count = 0
xml_dirs = file_name(annotation_folder)
print(xml_dirs)
label_temp = ''
for i in range(0, len(xml_dirs)):
	#print(xml_dirs[i])
	tree = ET.parse(xml_dirs[i])
	root = tree.getroot()
	label = root.find('filename').text
	# print(label)
	count_label = count

	#get the pictures' width and height
	for size in root.findall('size'):
		label_width = int(size.find('width').text)
		label_height = int(size.find('height').text)

	#get the boundbox's width and height
	for obj in root.findall('object'):
		for bbox in obj.findall('bndbox'):
			label_xmin = float((bbox.find('xmin').text))
			label_ymin = float((bbox.find('ymin').text))
			label_xmax = float((bbox.find('xmax').text))
			label_ymax = float((bbox.find('ymax').text))
			# print(label_xmin, label_ymin, label_xmax, label_ymax)
			if label_xmin<0 or label_xmax>label_width or label_ymin<0 or label_ymax>label_height or label_xmin>label_xmax or label_ymin>label_ymax:
				#judge the filename is not repeat
				bbox.find('xmin').text = str(int(float(bbox.find('xmin').text)) + 1)
				bbox.find('ymin').text = str(int(float(bbox.find('ymin').text)) + 1)
				bbox.find('xmax').text = str(int(label_width - 1))
				bbox.find('ymax').text = str(int(label_height - 1))

				print('--'*30)
				print(xml_dirs[i])   #print the xml's filename
				#print(label)
				print("width:",label_width)
				print("height:",label_height)
				print(label_xmin,label_ymin,label_xmax,label_ymax)
				print('--'*30)
				count = count+1
				# tree = ET.ElementTree(xml_dirs[i])
				tree.write(xml_dirs[i])
		# if label_temp == label:
		# 	continue
		label_temp = label

print("================================")
print(count)
