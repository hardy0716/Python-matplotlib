# -*- coding: utf-8 -*-
"""
Created on Wed May  4 20:23:41 2022

@author: 15517
"""

# conda install matplotlib #下载matplotlib包
# #终端输出命令：
# %matplotlib inline
# #新窗口输出命令：
# %matplotlib qt5


# 一、plt.bar()条形图
# bar(x, height, width=0.8, bottom=None, ***, align='center', data=None, **kwargs)
# 01.柱状图
import pandas as pd
import matplotlib.pyplot as plt
# 遇到数据中有中文的时候，一定要先设置中文字体
plt.rcParams['font.sans-serif']=['SimHei'] # 用黑体显示中文
# 解决坐标轴负号问题
plt.rcParams['axes.unicode_minus'] = False


data = pd.read_excel("D:/Desktop/matplotlib课件/01.柱状图.xlsx")
print(data)


# Pandas笔记7.1：数据排序,按分数这列，直接修改数据，降序
data.sort_values(by="分数",inplace=True,ascending=False)
print(data)

# 画柱状图：x轴是姓名，y轴是分类，颜色是红色，透明度0.5
plt.bar(data.姓名,data.分数,label="成绩",color="red",alpha=0.5) 

# lable的位置，左上角
plt.legend(loc="upper left")

# plt.show()
# 显示图例
# plt.legend()
# 设置X与Y轴的标题
plt.xlabel("姓名")
plt.ylabel("分数")
# 刻度标签及文字旋转
plt.xticks(data.姓名,rotation=45)
#y轴的刻度范围
plt.ylim([-20, 120])
# 紧凑型的布局
plt.tight_layout()
# 设置图表的标题、字号、粗体
plt.title("三年二班学生成绩",fontsize=32,fontweight='bold')

plt.savefig(r"d:\柱状图.jpg")
plt.show()


















