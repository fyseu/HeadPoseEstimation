'''
将pointing'04数据集中的txt文件整合到data文件夹下的csv文件中，将所有相关jpg图片复制到data文件夹下
'''
import numpy as np
import os
import csv
import shutil
import re

# csvFile = open('./face/file/csvFile.csv', 'w', newline='')
# writer = csv.writer(csvFile)
#
# for root, dirs, files in os.walk("./face/data"):
#     # print(root) #当前目录路径
#     # print(files) #当前路径下所有非目录子文件
#     for file in files:
#         if file.endswith('.txt'):
#             [i, f, x, y, w, h] = np.loadtxt(os.path.join(root, file), dtype=bytes).astype(str)
#             txt = [i, f, int(x), int(y), int(w), int(h)]
#             writer.writerow(txt)
#             print(file)
#         if file.endswith('.jpg'):
#             shutil.copyfile(os.path.join(root, file), os.path.join("./face/file/", file))
# csvFile.close()

'''
解析csv数据到相应格式
'''
csvFile0 = open('./face/file/val_labels_new.csv', 'w', newline='')
writer0 = csv.writer(csvFile0)
writer0.writerow(["image_name", "xmin", "xmax", "ymin", "ymax", "pitch", "yaw"])
csvFile1 = open('./face/file/train_labels_new1.csv', 'w', newline='')
writer1 = csv.writer(csvFile1)
writer1.writerow(["image_name", "xmin", "xmax", "ymin", "ymax", "pitch", "yaw"])
p1 = r"\+\d{1,2}|-\d{1,2}"
pattern1 = re.compile(p1)
csv_reader = csv.reader(open('./face/file/csvFile.csv', encoding='utf-8'))
k = 0
for row in csv_reader:
    if k < 186:  # Skip the first man
        k += 1
        label_str = pattern1.findall(row[0])
        writer0.writerow([row[0], int(row[2]) - int(row[4])/2, int(row[2]) + int(row[4])/2, int(row[3]) - int(row[5])/2, int(row[3]) + int(row[5])/2,
                          int(label_str[0])/100, int(label_str[1])/100])
    else:
        label_str = pattern1.findall(row[0])
        writer1.writerow([row[0], int(row[2]) - int(row[4])/2, int(row[2]) + int(row[4])/2, int(row[3]) - int(row[5])/2, int(row[3]) + int(row[5])/2,
                          int(label_str[0])/100, int(label_str[1])/100])
csvFile0.close()
csvFile1.close()
