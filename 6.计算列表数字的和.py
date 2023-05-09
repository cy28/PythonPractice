numbers = []  # 定义一个空列表来存储输入的数字

while True:
    user_input = input("请输入一个数字（按 q 键结束输入）：")

    if user_input.lower() == 'q':
        break  # 如果用户输入 q，跳出循环
    else:
        try:
            number = float(user_input)  # 尝试将用户输入的字符串转换成浮点数
            numbers.append(number)  # 将转换后的数字添加到列表中
        except ValueError:
            print("请输入有效的数字！")

print("输入的数字列表为：", numbers)



























