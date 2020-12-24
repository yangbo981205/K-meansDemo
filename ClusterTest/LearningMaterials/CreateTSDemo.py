import numpy as np
import pandas as pd
from pandas.tseries.offsets import *
from datetime import datetime

# 将datetime转换成timestamp
print(pd.to_datetime("19981205"))
print(pd.to_datetime("1998-12-05"))
print(pd.to_datetime("12/05/1998"))
a_list = ["19981205", "19981206", "19981207"]
print(pd.to_datetime(a_list))

# 创建时间序列类型的series对象
print(pd.Series([11, 22, 33], index=pd.to_datetime(a_list)))

# datetime列表
date_list = [datetime(2020, 1, 1), datetime(2020, 1, 2), datetime(2020, 1, 3),
             datetime(2020, 1, 4), datetime(2020, 1, 5), datetime(2020, 1, 6)]
# 创建series
print(pd.Series(np.arange(6), index=date_list))

# DataFrame类型时序数据
data_demo = [[11, 22, 33], [44, 55, 66], [77, 88, 99], [12, 13, 45], [15, 16, 17], [18, 19, 12]]
print(pd.DataFrame(data=data_demo, index=date_list))

# 创建固定频率的时间序列
'''
data_range(start= , end= , periods= , freq= , tz= , normalize= , name= , closed= , **kwargs)
**以下四个参数至少指定两个个，否则会报错**
start: 起始日期，默认None
end: 终止日期，默认None
periods: 表示产生多少各时间索引值，个数
freq: 用来指定计时单位，默认为D表示天  W-SUN表示每周的星期日

normalize: 将时间规范化到 00:00
'''
print(pd.date_range(start="20200101", end="20200110"))
print(pd.date_range(start="20200101", periods=5))
print(pd.date_range(end="20200101", periods=10))
print(pd.date_range(start="20200101", periods=10, freq='W-SUN'))
print(datetime.now())
print(pd.date_range(start=datetime.now(), periods=10, freq='D', tz="Asia/Hong_Kong"))
print(pd.date_range(start=datetime.now(), periods=10, freq='D', normalize=True, tz="Asia/Hong_Kong"))

'''
freq指定偏移量 
时间序列的基础频率：D天，B工作日，H小时，T/min分，S秒，L/ms毫秒，U微秒，M每月最后一天  组合使用：BM，MS，BMS
'''
print(pd.date_range(start="20200101", periods=5, freq='5h'))

print(pd.date_range(start="20200101", end="20200310", freq='5D'))
date_offset = DateOffset(months=1, days=5)
print(date_offset)
print(Week(2)+Hour(10))
print(pd.date_range(start="20200101", periods=5, freq=date_offset))
print(pd.date_range(start="20200101", periods=5, freq=Week(2)+Hour(10)))

# 创建时期对象
date_period = pd.Period("2020", "M")  # 默认为最精确位，或指定
print(date_period+1)
print(date_period+2)
print(date_period+3)
date_period1 = pd.Period(202101, freq='M')
print(date_period1 - date_period)
period_index = pd.period_range('2020-01-01', '2020-05-01', freq='M')
print(period_index)
str_list = ['2010', '2011', '2012']
print(pd.PeriodIndex(str_list, freq='A-DEC'))
print(pd.Series(np.arange(5), period_index))

# 时期的频率转换
period = pd.Period('2017', freq='A-DEC')
print(period)
print(period.asfreq('M', how='start'))
print(period.asfreq('M', how='end'))





