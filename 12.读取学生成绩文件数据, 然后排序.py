"""
输入文件:
    三列: 学号 姓名 成绩
    列之间用逗号隔开, 比如101, 小张, 88
    行之间用\n分割
处理:
    读取文件, 按成绩倒序排列
输出:
    排序后的三列数据

"""


# 1. 读取文件, 得到一个装有数据的列表
def read_file():
    content = []
    with open('student_grade12', 'r', encoding='utf-8') as read_stream:
        for line in read_stream:
            line = line[:-1]  # 去掉每一行的换行符
            content.append(line.split(','))  # 将每一行进行拆分, 每一行变成一个列表, 列表中有三个元素
    return content


data = read_file()
print(data)
# [['101', ' 小a', ' 88'], ['101', ' 小b', ' 77']......


# 2. 对数据进行排序, 得到一个排序后的列表
def sort_grade(data):
    return sorted(data, key=lambda x: int(x[2]), reverse=True)


grade_list = sort_grade(data)
print(grade_list)
# [['101', ' 小c', ' 99'], ['101', ' 小a', ' 88'], ['101', ' 小b', ' 77'], ['101', ' 小d', ' 66'], ['101', ' 小e', ' 55'], ['101', ' 小f', ' 44']]


# 写出文件
def write_file(data):
    with open('grade_list12', 'w', encoding='utf-8') as write_stream:
        for i in data:
            write_stream.write(','.join(i) + '\n')


write_file(grade_list)










