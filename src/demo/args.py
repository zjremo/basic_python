import time

def great(name: str, age: int) -> str:
    return f"Hello, {name}! You are {age} years old."

def create_profile(name: str, age: int, email: str):
    print(f'name:{name}')
    print(f'age:{age}')
    print(f'email:{email}')

start = time.perf_counter()
person = ['John', 20]
print(great(*person))

list1 = [1, 2, 3]
tuple1 = (4, 5, 6)

merged = [*list1, *tuple1]
print(merged)

profile = {
    'name': 'John',
    'age': 20,
    'email': 'john@example.com'
}
create_profile(**profile)
end = time.perf_counter()
print(f'Time taken: {end - start:.6f} seconds')