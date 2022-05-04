# -*- coding: utf-8 -*-
"""
Created on Wed May  4 20:45:36 2022

@author: 15517
"""

# 需要把：orientation="horizontal"，然后x,与y的数据交换，再添加bottom=x,即可
# 水平条形图注意：刻度标签需要垂直居中显示

import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib qt5
# 遇到数据中有中文的时候，一定要先设置中文字体
plt.rcParams['font.sans-serif']=['SimHei'] # 用黑体显示中文
数据 = pd.read_excel("D:/Desktop/matplotlib课件/01.柱状图.xlsx")
# Pandas笔记7.1：数据排序,按分数这列，直接修改数据，降序
数据.sort_values(by="分数",inplace=True,ascending=False)
# 画水平条形图:x=起始位置，bottom=水平条的底部（左侧），y轴。heith=水平条的宽度，width=水平条长度
# orientation="horizontal" 定义为水平条
plt.bar(x=0,bottom=数据.姓名,height=0.5,width=数据.分数,orientation="horizontal",color="red",alpha=0.5)
# 设置X与Y轴的标题
plt.xlabel("姓名")
plt.ylabel("分数")
# 文字旋转
# plt.xticks(数据.姓名,rotation="90")
# 紧凑型的布局
plt.tight_layout()
# 设置图表的标题
plt.title("三年二班学生成绩",fontsize=16)
plt.show()


