"""
1. read() 方法：
read() 方法用于从文件中读取指定数量的字节或者全部内容（如果未指定字节数）。
语法为 file.read(size)，其中 size 是要读取的字节数。如果省略 size 参数或将其设置为负数，read() 方法将读取整个文件。
该方法返回一个字符串，包含从文件中读取的内容。

示例：
file = open('example.txt', 'r')
content = file.read()  # 读取整个文件的内容
print(content)
file.close()

"""


"""
2. readline() 方法：
readline() 方法用于从文件中逐行读取内容，每次读取一行。
语法为 file.readline()。该方法返回一个字符串，包含当前行的内容。
每次调用 readline() 方法，文件对象会记录当前读取位置，下一次调用 readline() 会从上一次读取位置之后的下一行开始。

示例:
file = open('example.txt', 'r')
line1 = file.readline()  # 读取第一行
line2 = file.readline()  # 读取第二行
print(line1)
print(line2)
file.close()

"""

"""
3. readlines() 方法：
readlines() 方法用于从文件中读取所有行，并将每一行作为一个元素存储在一个列表中。
语法为 file.readlines()。该方法返回一个列表，列表中的每个元素对应文件的一行。
# # ['hello 第66个python文件\n', 'helloworld']

示例:

file = open('example.txt', 'r')
lines = file.readlines()  # 读取所有行
for line in lines:
    print(line)
file.close()


"""











