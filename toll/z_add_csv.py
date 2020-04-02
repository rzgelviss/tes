path1 = './labels_img.csv'
path2 = './label2.csv'
with open(path2, 'a') as f2:
    with open(path1, 'r') as f1:
        lines = f1.readlines()
        lines = lines[1:]
        for line in lines:
            f2.write(line)
