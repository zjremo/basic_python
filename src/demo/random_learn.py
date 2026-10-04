import random

random.seed(10)
print(random.random())
print(random.randint(1, 10))
print(random.randrange(1, 10, 2))
print(random.choice([1, 2, 3, 4, 5]))
print(random.choices([1, 2, 3, 4, 5], k=3))
l = [1, 2, 3, 4, 5]
print(f"before shuffle: {l}")
random.shuffle(l)
print(f"after shuffle: {l}")
print(random.sample([1, 2, 3, 4, 5], k=3))
print(random.uniform(1, 10))