from dataclasses import dataclass, field
import random
from typing import ClassVar

@dataclass(order=True)
class Person:
    name: str
    age: int = field(repr=False) # 打印时是否要显示这个字段
    height: int = field(default_factory=lambda: random.randint(150, 200))
    people_num: ClassVar[int] = 0

    # 初始化__init__后执行
    def __post_init__(self):
        Person.people_num += 1

class NormalPerson:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
normal_person = NormalPerson('John', 30)
print(normal_person)

person = Person(name='Alice', age=30)
print(person)
person2 = Person(name='Alice', age=32)
print(person2)

print(person > person2)
