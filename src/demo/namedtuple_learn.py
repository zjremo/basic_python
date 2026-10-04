from typing import NamedTuple

# 元类(元组是不可变的)，十分类似Java中的record类
class Point(NamedTuple):
    x: float
    y: float 

p = Point(x=1.0, y=2.0)
print(f'p.x: {p.x}, p.y: {p.y}')
print(f'p[0]: {p[0]}, p[1]: {p[1]}')