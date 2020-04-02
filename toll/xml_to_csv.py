import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(float(member[4][0].text)),
                     int(float(member[4][1].text)),
                     int(float(member[4][2].text)),
                     int(float(member[4][3].text))
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']

    xml_df = pd.DataFrame(xml_list, columns=column_name)
    print(xml_df)
    return xml_df


def main():
    # for folder in ['train','test']:
    #     image_path = os.path.join(os.getcwd(), ('images/' + folder))

    # image_path = os.path.join(os.getcwd(), ('images/' + folder))  # 这里就是需要访问的.xml的存放地址
    image_path = r'E:\data\打标\20191029\zhou2(1)\33\zhou5-PascalVOC-export\Annotations'
    xml_df = xml_to_csv(image_path)                               # object_detection/images/train or test
    xml_df.to_csv(('images/' + 'labels.csv'), index=None)
    print('Successfully converted xml to csv.')


main()
