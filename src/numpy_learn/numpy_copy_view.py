import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print('This is copy demo: make a copy of the original array')
x = arr.copy()
arr[0] = 42
print('after change arr[0] = 42, arr:', arr)
print('after change arr[0] = 42, x:', x)

print('This is view demo: make a view of the original array')
y = arr.view()
y[0] = 43
print('after change y[0] = 43, arr:', arr)
print('after change y[0] = 43, y:', y)

# check if x and y are the same array
print('x is the same array as arr:', x is arr)
print('y is the same array as arr:', y is arr)
print('x is the same array as y:', x is y)

# get base of x and y
print('base of x(a copy of the original array):', x.base)
print('base of y(a view of the original array):', y.base)