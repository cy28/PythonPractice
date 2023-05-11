with open('grade_list17', 'r', encoding='utf-8') as fin:
    # 读取每一行
    for line in fin:
        # 去掉行尾的换行符
        line = line[:-1]
        number, name, course, grade = line.split(',')

        print(number)
        print(name)
        print(course)
        print(grade)