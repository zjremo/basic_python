import numpy as np

# 1-d array
arr = np.array([1, 2, 3, 4, 5])
print(arr[1:5])
print(arr[1:])
print(arr[:4])
print(arr[:])
print(arr[-3:-1])
print(arr[-3:])
print(arr[:-3])
print(arr[:-3])

print(arr[1:5:2])
print(arr[::2])

# 2-d array
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4]) # 7, 8, 9
print(arr[0:2, 2]) # 3, 8
print(arr[0:2, 1:4]) # [[2, 3, 4], [7, 8, 9]]