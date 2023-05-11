"""
需求:
将 teacher_list18中老师的名字与grade_list17中的对应数据根据学科相关联, 加在每一行的后面
"""
# 本质上将一个文件写成字典, 给另一个文件使用


# 1. 将老师的list 根据学科构成一个字典

teacher_dict = {}

with open('teacher_list18', 'r', encoding='utf-8') as fin:
    for line in fin:
        # 去掉换行符
        line = line.strip()
        # 或者 line = line[:-1]
        # 将每行拆分, 赋给teacher_name和course
        course, teacher_name = line.split(' ')
        # 放到字典中
        teacher_dict[course] = teacher_name
print(teacher_dict)


# 2. 将字典中的老师元素, 在输出时, 打印在后面

with open('grade_list17', 'r', encoding='utf-8') as fin:
    # 读取每一行
    for line in fin:
        # 去掉行尾的换行符
        # line = line[:-1]
        line = line.strip()
        number, name, course, grade = line.split(' ')
        # 每一行根据科目, 在上面构成的字典中得到老师的名字
        teacher = teacher_dict.get(course)

        print(number, name, course, grade, teacher)










