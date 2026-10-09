import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4) # 返回所有等于4的元素的索引
print(x)

x = np.where(arr % 2 == 0) # 返回所有偶数的索引
print(x)

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right') # 返回7在arr中的索引, side='right'表示返回大于等于7的第一个元素的索引（从右边开始查找）
print(x)