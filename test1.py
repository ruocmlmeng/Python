# -*- coding: UTF-8 -*- #
"""
@filename:test1.py
@author:WangJun
@time:2024-06-02
"""
import numpy as np  # 导入需要的库
data1 = np.loadtxt("heart_failure_clinical_records_dataset.csv",delimiter=",",skiprows=1, dtype=float)   # 读取数据文件，将本行代码补充完整
data1[:, 2] = np.round(data1[:, 2] / 1000, 1)  # 根据题目要求计算，将本行代码补充完整
x_train = data1[:210, :-1]  # 获取x的训练集数据，将本行代码补充完整
y_train = data1[:210, -1]   # 获取y的训练集数据，将本行代码补充完整
x_test = data1[210:, :-1]   # 获取x的测试集数据，将本行代码补充完整
y_test = data1[210:, -1]    # 获取y的测试集数据，将本行代码补充完整
sodium = np.median(x_test[:,8])
print("血清钠含量中位数是：",sodium)
train_smoke = x_train[x_train[:, 9] == 1]  # 找出符合要求的数据，将本行代码补充完整
total_smokers = np.sum(train_smoke[:, 9] == 1)
print("抽烟的患者有多少人：",total_smokers)
np.savetxt("result1.csv", x_test, delimiter=",", fmt="%.2f")  # 将数组保存为文件，将本行代码补充完整