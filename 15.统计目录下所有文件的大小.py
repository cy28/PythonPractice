import os

# 1. 打印一个文件的大小
print(os.path.getsize('1.两数之和.py'))  # 198  单位是字节

# 打印一个目录中所有的文件
sum_size = 0
for file in os.listdir('.'):
    if os.path.isfile(file):  # 不加这句会有一些配置文件也被打印
        print(file)
        sum_size += os.path.getsize(file)
print(f'目录文件的总大小是({sum_size}/1000)KB')






















