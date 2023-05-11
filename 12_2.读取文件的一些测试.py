
# 1. 注意: 这样打开每一个元素有一个换行符
with open('student_grade12', 'r', encoding='utf-8') as read_stream:
    content1 = read_stream.readlines()
    print(content1)
# 读取得到的是由字符串构成的列表
#  ['101, 小a, 88\n', '101, 小b, 77\n', '101, 小c, 99\n', '101, 小d, 66\n', '101, 小e, 55\n', '101, 小f, 44\n']


# 2. 跟上面的方法读出同样的结果
with open('student_grade12', 'r', encoding='utf-8') as read_stream:
    content2 = []
    for line in read_stream:
        content2.append(line)
print(content2)
# ['101, 小a, 88\n', '101, 小b, 77\n', '101, 小c, 99\n', '101, 小d, 66\n', '101, 小e, 55\n', '101, 小f, 44\n']

# 3. 将大列表的每一个元素进行拆分, 即将每一行进行拆分
with open('student_grade12', 'r', encoding='utf-8') as read_stream:
    content3 = []
    for line in read_stream:

        content3.append(line.split(','))
print(content3)
# [['101', ' 小a', ' 88\n'], ['101', ' 小b', ' 77\n'], ['101', ' 小c', ' 99\n'], ['101', ' 小d', ' 66\n'], ['101', ' 小e', ' 55\n'], ['101', ' 小f', ' 44\n']]











