import numpy as np

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]

newarr = arr[x]
print(newarr)

filter = arr > 42
print(filter) # [ False  False  True  True]
newarr = arr[filter]
print(newarr) # [43 44]