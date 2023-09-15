import numpy as np

''''np.ceil 是 NumPy 中的一个函数，用于向上取整（ceiling）操作。它将输入数组中的每个元素取向最接近的整数，该整数不小于该元素。
如果元素是正数（大于零），则向上取整为不小于该元素的最小整数。
如果元素是负数（小于零），则向上取整为不小于该元素的最大整数。
如果元素是零，则仍然是零。
'''''
x = np.array([1.2, 2.7, -3.4, 0.0, 5.1])
result = np.ceil(x)
print(result)  # [ 2.  3. -3.  0.  6.]


''''np.nanmean 是 NumPy 库中的一个函数，用于计算数组中的平均值，但会忽略数组中的 NaN（Not-a-Number） 值。NaN 常常表示缺失的数据或无效的数据。'''
arr = np.array([1.0, 2.0, np.nan, 4.0, 5.0])

# 计算数组的平均值，忽略 NaN 值
mean_value = np.nanmean(arr)
print(mean_value)  # 输出: 3.0