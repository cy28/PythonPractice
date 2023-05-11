"""
python读取文件的两个方法:

方法1 按行读 有一个问题会读到换行符
    for line in fin

方法2 一次读取所有的内容到一个字符串
    content = fin.read()

"""
import os

# 传入要合并的txt文件所在的大目录的路径
data_dir = './many_texts19'

content = []

for file in os.listdir(data_dir):
    # 每一个文件的路径
    file_path = f"{data_dir}/{file}"
    # 判断是否是文件, 然后是否以txt结尾
    if os.path.isfile(file_path) and file.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as fin:
                # print(fin.read())
                content.append(fin.read())  # 读了三个字符串进到content

final_content = '\n \n'.join(content)  # 由三个大字符串构成列表, 通过换行符构成一个大字符串
# print(final_content)

# 将这个大字符串写入一个文件中

with open('./many_texts19/combine_txt', 'w', encoding='utf-8') as f_out:
    f_out.write(final_content)






























