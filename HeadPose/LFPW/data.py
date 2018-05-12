import numpy as np
import os
import csv
import scipy.io as sio

mat = sio.loadmat("./300W-LP/LFPW/LFPW_image_test_0001_0.mat")
# [pitch yaw roll tdx tdy tdz scale_factor]
pre_pose_params = mat['Pose_Para'][0]
# Get [pitch, yaw, roll, tdx, tdy]
pose_params = pre_pose_params[:]
print(mat["pt2d"])
print(pre_pose_params)