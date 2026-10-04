import random
def generate_numbers(n: int):
    while n > 0:
        yield random.randint(1, 100)
        n -= 1

generator = generate_numbers(5)
print(next(generator))
for number in generator:
    print(number, sep=' ', end=' ')