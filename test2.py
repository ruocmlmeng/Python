# -*- coding: UTF-8 -*- #
"""
@filename:test2.py
@author:WangJun
@time:2024-06-02
"""
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.unicode.east_asian_width", True)
plt.rcParams['font.sans-serif'] = ['SimHei']

DF2A = pd.read_excel("guangdong.xlsx",sheet_name="population",usecols=[0,1])
DF2B = pd.read_excel("guangdong.xlsx",sheet_name="health")

DF2B["人均执业医师数"] = (DF2B["执业(助理)医师数"] / DF2A["常住人口"] * 1000).round(2)
DF2B["人均注册护士数"] = (DF2B["注册护士数"] / DF2A["常住人口"] * 1000).round(2)

DF2C = DF2B[["年份", "人均执业医师数", "人均注册护士数"]]
print(DF2C)

y1 = DF2C["人均执业医师数"]
y2 = DF2C["人均注册护士数"]
y3 = 4.7 - DF2C["人均注册护士数"]
x = list(range(9))

plt.plot(x, y1,"b-o", label="人均执业医师数")
plt.bar(x, y2, color="pink", edgecolor="purple", width=0.6,label="人均注册护士数")
plt.plot(x, y3,"m:p", label="差额")

plt.ylabel("人/千人")
xtick_labels = ["2011年","2013年","2015年","2017年","2019年"]
plt.xticks([0,2,4,6,8], xtick_labels)
plt.legend()

plt.show()