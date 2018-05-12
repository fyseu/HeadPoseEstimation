'''
将LFPW数据集中的mat文件整合到data文件夹下的csv文件中，将所有相关jpg图片复制到data文件夹下
'''
import numpy as np
import os
import csv
import scipy.io as sio
import shutil

csvFile0 = open('./data/val_labels.csv', 'a', newline='')
writer0 = csv.writer(csvFile0)
# writer0.writerow(["image_name", "xmin", "xmax", "ymin", "ymax", "pitch", "yaw", "roll"])
csvFile1 = open('./data/train_labels.csv', 'a', newline='')
writer1 = csv.writer(csvFile1)
# writer1.writerow(["image_name", "xmin", "xmax", "ymin", "ymax", "pitch", "yaw", "roll"])
for root, dirs, files in os.walk("./300W-LP/LFPW_Flip/"):
    # print(root) #当前目录路径
    # print(files) #当前路径下所有非目录子文件
    for file in files:
        if file.endswith('.mat'):
            mat = sio.loadmat(os.path.join(root, file))
            # [pitch yaw roll tdx tdy tdz scale_factor]
            pre_pose_params = mat['Pose_Para'][0]
            # Get [pitch, yaw, roll, tdx, tdy]
            pose_params = pre_pose_params[:]
            xmin = int(min(mat['pt2d'][0]))
            xmax = int(max(mat['pt2d'][0]))
            ymin = int(min(mat['pt2d'][1]))
            ymax = int(max(mat['pt2d'][1]))
            pitch = (pose_params[0] * 180 / np.pi)
            yaw = (pose_params[1] * 180 / np.pi)
            roll = (pose_params[2] * 180 / np.pi)
            image_name = file[:-4] + "_flip.jpg"
            data = [image_name, xmin, xmax, ymin, ymax, pitch, yaw, roll]
            print(image_name)
            if "test" in file:
                writer0.writerow(data)
            if "train" in file:
                writer1.writerow(data)
        # if file.endswith('.jpg'):
        #     image_name = file[:-4] + "_flip.jpg"
        #     shutil.copyfile(os.path.join(root, file), os.path.join("./data/", image_name))
csvFile0.close()
csvFile1.close()

# '''
# 解析csv数据到相应格式
# '''
# csvFile0 = open('./face/file/val_labels_new.csv', 'w', newline='')
# writer0 = csv.writer(csvFile0)
# writer0.writerow(["image_name", "xmin", "xmax", "ymin", "ymax", "pitch", "yaw"])
# csvFile1 = open('./face/file/train_labels_new1.csv', 'w', newline='')
# writer1 = csv.writer(csvFile1)
# writer1.writerow(["image_name", "xmin", "xmax", "ymin", "ymax", "pitch", "yaw"])
# p1 = r"\+\d{1,2}|-\d{1,2}"
# pattern1 = re.compile(p1)
# csv_reader = csv.reader(open('./face/file/csvFile.csv', encoding='utf-8'))
# k = 0
# for row in csv_reader:
#     if k < 186:  # Skip the first man
#         k += 1
#         label_str = pattern1.findall(row[0])
#         writer0.writerow([row[0], int(row[2]) - int(row[4])/2, int(row[2]) + int(row[4])/2, int(row[3]) - int(row[5])/2, int(row[3]) + int(row[5])/2,
#                           int(label_str[0])/100, int(label_str[1])/100])
#     else:
#         label_str = pattern1.findall(row[0])
#         writer1.writerow([row[0], int(row[2]) - int(row[4])/2, int(row[2]) + int(row[4])/2, int(row[3]) - int(row[5])/2, int(row[3]) + int(row[5])/2,
#                           int(label_str[0])/100, int(label_str[1])/100])
# csvFile0.close()
# csvFile1.close()
