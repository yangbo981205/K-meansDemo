import numpy as np
import pandas as pd
from datetime import datetime

# 通过时间戳索引选取子集
date_list = [datetime(2020, 5, 1), datetime(2020, 1, 2), datetime(2020, 7, 3),
             datetime(2020, 1, 4), datetime(2020, 12, 5), datetime(2020, 1, 6)]

# 将日期字符串列表转换为DatetimeIndex类型的对象
date_index = pd.to_datetime(date_list)
print(date_index)
date_series = pd.Series(np.arange(6), index=date_index)
print(date_series)

# 根据位置索引获取数据
print(date_series[2])

# 根据时间戳索引获取数据
date_time = datetime(2020, 12, 5)
print(date_series[date_time])
print(date_series["2020-01-03"])

# truncate完成数据截取
ret = date_series.sort_index()

print(ret)  # 按时间戳索引排序
print(ret.truncate(before="20200703"))  # 之后的数据，包含本身
print(ret.truncate(after="20200703"))  # 之前的数，包含本身
