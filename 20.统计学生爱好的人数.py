
hobbies = {}

with open('student_hobby20', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()  # 去除行首尾的空格和换行符
        items = line.split()  # 按空格分割行，得到一个列表
        name = items[0]  # 第一个元素是姓名
        for hobby in items[1:]:  # 从第二个元素开始遍历，即爱好列表
            if hobby in hobbies:
                hobbies[hobby] += 1  # 如果爱好已经存在于字典中，人数加一
            else:
                hobbies[hobby] = 1  # 如果爱好不存在于字典中，添加该爱好并初始化人数为一

# 打印统计结果
for hobby, count in hobbies.items():
    print(f'{hobby}: {count}人')









