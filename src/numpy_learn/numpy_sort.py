import numpy as np

# Return a sorted copy of an array.
arr = np.array(
    [("Alice", 20), ("Bob", 18)],
    dtype=[('name', 'U10'), ('age', 'i4')]
)
np.sort(arr, order='name') # 按 age 字段排序