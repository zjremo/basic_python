from contextlib import contextmanager
import time
import os
from dotenv import load_dotenv

# method1：function-based context manager
load_dotenv()

@contextmanager
def add_to_list(item: int, lst: list[int] = None):
    try:
        if lst is None:
            lst = []
        lst.append(item + 1)
        yield lst
        lst.remove(item + 1)
    except Exception as e:
        print(f'Error adding item to list: {e}')
    finally:
        lst.append(item)
        print(f'List: {lst}')

with add_to_list(1) as lst:
    print(f'List: {lst}')

@contextmanager
def timer():
    try:
        start = time.perf_counter()
        yield
    finally:
        end = time.perf_counter()
        print(f'Time taken: {end - start:.6f} seconds')

with timer():
    time.sleep(1)

@contextmanager
def set_temporary_env(**kwargs):
    try:
        original_env = os.environ.copy()
        os.environ.update(kwargs)
        yield
        print('after yield')
    finally:
        os.environ.clear()
        os.environ.update(original_env)

print(os.environ.get('TEST_VAR'))
with set_temporary_env(TEST_VAR='abaaba'):
    print(os.environ.get('TEST_VAR'))
print(os.environ.get('TEST_VAR'))

# method2：class-based context manager
class ContextTest:
    def __init__(self):
        self.value = 0
        print(f'ContextTest initialized with value: {self.value}')

    def __enter__(self):
        print('Entering context')
        self.value += 1
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print('Exiting context')
        if exc_type is not None:
            print(f'Exception type: {exc_type}')
            print(f'Exception value: {exc_value}')
            print(f'Traceback: {traceback}')
        return True

context_test = ContextTest()
with context_test as ctx:
    print(f'ContextTest value: {ctx.value}')
    raise Exception('Test exception')
print(f'ContextTest value: {context_test.value}')