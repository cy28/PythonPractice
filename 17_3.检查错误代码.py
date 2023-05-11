with open('grade_list17', 'r', encoding='utf-8') as fin:
    # 读取每一行
    for line in fin:
        # 去掉行尾的换行符
        line = line.strip()

        # 拆分行为字段
        fields = line.split(' ')

        # 检查字段数量是否符合预期
        if len(fields) != 4:
            print(f"Skipping line: {line}. Expected 4 fields, found {len(fields)} fields.")
            continue

        # 将字段赋值给相应的变量
        number, name, course, grade = fields

        # 打印值
        print(number)
        print(name)
        print(course)
        print(grade)
