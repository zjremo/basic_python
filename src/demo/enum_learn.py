from enum import Enum

"""唯一实例"""
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

    @classmethod
    def print_member(cls):
        for c in cls:
            print(c.name, c.value)
    
    def __eq__(self, value: object, /) -> bool:
        if isinstance(value, Color):
            return self.value == value.value
        elif isinstance(value, int):
            return self.value == value
        else:
            return False

Color.print_member()
print(Color.RED == 1)