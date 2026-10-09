import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# 默认axis为0, 上下拼接，即垂直拼接 
arr = np.concatenate((arr1, arr2))
print(arr) # [1 2 3 4 5 6]

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# axis为1, 左右拼接，即水平拼接
c = np.concatenate((a, b), axis=1)
print(c) # [[1 2 5 6] [3 4 7 8]]

"""
concatenate: 在已有的轴上接长，维度(ndim)不变
stack: 沿新的轴堆起来, 维度会+1
"""
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=0)
print(arr) # [[1 2 3] [4 5 6]]
arr = np.stack((arr1, arr2), axis=1)
print(arr) # [[1 4] [2 5] [3 6]]