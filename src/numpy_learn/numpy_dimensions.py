import numpy as np

# 0-d array
arr = np.array(42)
print(arr)
print(type(arr))

# 1-d array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# 2-d array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# ndim: 取到一个元素要几层索引
print("arr.ndim:", arr.ndim)

# 3-d array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)
print("arr.ndim:", arr.ndim)
print(arr.shape)