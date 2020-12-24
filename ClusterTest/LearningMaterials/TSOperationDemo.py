import numpy as np
import pandas as pd
import datetime
from pandas.tseries.offsets import *
from datetime import datetime

# 时间序列移动
'''
前移或后移数据
shift(periods=1, freq=None, axis=0)
periods：移动的幅度，移动多少个，默认为1
freq：按照指定的频率进行移动
axis：轴
'''
date_index = pd.date_range(start="20200101", periods=5)
date_series = pd.Series(np.arange(5)+1, index=date_index)
print(date_series)
print(date_series.shift(1))  # 向后移动1
print(date_series.shift(-1))  # 向前移动1
