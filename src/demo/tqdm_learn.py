from tqdm import tqdm
import time

tasks = ['task1', 'task2', 'task3', 'task4', 'task5']

with tqdm(tasks) as pbar:
    for task in pbar:
        pbar.set_description(f'Processing {task}')
        time.sleep(0.8)

print('All tasks completed')
