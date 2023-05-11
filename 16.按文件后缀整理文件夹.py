# 1. 现将要整理的目录保存起来
import os
import shutil

dir = 'arrange_dir16'

# 2.

for file in os.listdir(dir):
    # 拆分后的元组, 只要扩展名的字符串, 取到文件的扩展名
    ext = os.path.splitext(file)[-1]
    # 利用字符串切片, 把前面的.去掉
    ext = ext[1:]
    # 以扩展名创建目录, 如果没有这个文件夹, (那么not后面就是空, if 非空), 就会执行后面的创建目录的代码
    if not os.path.isdir(f"{dir}/{ext}"):
        os.mkdir(f"{dir}/{ext}")

    source_path = f"{dir}/{file}"  # 实际上这是一个完整的路径
    target_path = f"{dir}/{ext}/{file}"
    # 将源文件移动到创建的目录中
    shutil.move(source_path, target_path)
























