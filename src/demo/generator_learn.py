import random
def generate_numbers(n: int):
    while n > 0:
        yield random.randint(1, 100)
        n -= 1

generator = generate_numbers(5)
print(next(generator))
for number in generator:
    print(number, sep=' ', end=' ')
print()

# 生成器来读取文件行，避免一次性读入所有数据
def readlines(file_path: str):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line

lines = readlines('open_file.txt')
for line in lines:
    print('line:', line, end='')
print()