import psutil

# cpu信息
print(f'cpu_count: {psutil.cpu_count()}')
print(f'cpu_percent: {psutil.cpu_percent()}')

# disk信息
print(f'disk_usage: {psutil.disk_usage("./src")}')

# memory信息
print(f'memory_info: {psutil.virtual_memory()}')

"""
Output:
cpu_count: 16
cpu_percent: 0.0
disk_usage: sdiskusage(total=253672550400, used=138836959232, free=114835591168, percent=54.7)
memory_info: svmem(total=33827909632, available=11424264192, percent=66.2, used=22403645440, free=11424264192)
"""