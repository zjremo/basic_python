class add:
    def __init__(self, val:int):
        self.val = val

    def __add__(self, val:int):
        num = self.val + val
        return add(num)

    def __call__(self, val:int):
        num = self.val + val
        return add(num)

    def __str__(self):
        return f'{self.val}'

addTwo = add(2)
print(addTwo)
print(addTwo + 5)
print(addTwo(3))
print(addTwo(3)(5))

print(add(1)(2))
print(add(1)(2)(3))
print(add(1)(2)(3)(4))
print(add(1)(2)(3)(4)(5))