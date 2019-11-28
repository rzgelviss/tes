import re


with open('./class-descriptions-boxable.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        # print(line)
        r = re.findall(r'(.*boat.*)', line, re.I) # 不区分大小写
        if r != []:
            print(r)
            label = r[0].split(',')[0]
            print(label)