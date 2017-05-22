import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# df = pd.read_csv('power.csv')
# for i in range(1, 1454, 10):
#     data = df.iloc[:, i]
#     data = np.array(data)
#     plt.plot(data)
#     plt.show()


data = pd.read_csv('power_total.csv', encoding='gbk', index_col='date')
data.index = pd.to_datetime(data.index)  # 将字符串索引转换成时间索引
data = data['value']
data = data.astype('float')
# data.sort_index()
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
plt.rcParams['axes.unicode_minus'] = False  # 显示小数
# 时序图
data.plot()
plt.show()


