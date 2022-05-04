# -*- coding: utf-8 -*-
"""
Created on Wed May  4 21:51:32 2022

@author: 15517
"""

# #终端输出命令：
# %matplotlib inline
# #新窗口输出命令：
# %matplotlib qt5

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# 遇到数据中有中文的时候，一定要先设置中文字体
plt.rcParams['font.sans-serif']=['SimHei'] # 用黑体显示中文
数据 = pd.read_excel("D:/Desktop/matplotlib课件/03.分组柱状图.xlsx")
数据.sort_values(by='第二年',inplace=True,ascending=False)
print(数据)
# 把dataframe转换为list
x = 数据['姓名'].values.tolist()
y1 = 数据['第一年'].values.tolist()
y2 = 数据['第二年'].values.tolist()
宽度=0.3
plt.bar(x=x,height=y1,label="第一年",color="red",width=宽度)
# Numpy笔记1.1.1
plt.bar(x=np.arange(len(x))+宽度,height=y2,label="第二年",color="blue",width=宽度)
# lable的位置，右上角
plt.legend(loc="upper right")
# plt.xticks可以实现旋转角度，但是不能设置旋转点，所以要与轴.set_xticklabels配合使用
plt.xticks(x)
# 对轴进行操作,需要先拿到轴
轴=plt.gca()
# 对x轴数据进行旋转45度，且以中心为旋转点【同样可以用left或right】
轴.set_xticklabels(x,rotation=45,ha="center")
# 解决图四周的空白，是对图形操作，需要先拿到图形[也可以用紧凑型布局方案]
图形=plt.gcf()
图形.subplots_adjust(left=0.1,bottom=0.3)
# 紧凑型的布局
#plt.tight_layout()
plt.show()
