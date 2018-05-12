import glob as gb
import cv2
import csv
from utils import draw_axis

cv2.namedWindow('window_frame')
img_path = gb.glob("./data/*.jpg")

# 从文件读取
reader = csv.reader(open('./data/val_labels.csv', 'r'))

for line in reader:
    print(reader.line_num)
    # 忽略第一行
    if reader.line_num == 1:
        continue
    img_name = line[0]
    xmin = int(line[1])
    xmax = int(line[2])
    ymin = int(line[3])
    ymax = int(line[4])
    pitch = float(line[5])
    yaw = float(line[6])
    roll = float(line[7])
    img = cv2.imread("./data/"+img_name)
    img = cv2.rectangle(img, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)
    img = draw_axis(img, yaw, pitch, roll, tdx = (xmin + xmax)/2, tdy= (ymin + ymax)/2, size=50)
    cv2.imshow('window_frame', img)

    if cv2.waitKey(200) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()