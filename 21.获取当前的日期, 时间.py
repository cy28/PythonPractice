import datetime

curr_datetime = datetime.datetime.now()

print(curr_datetime, type(curr_datetime))
# 2023-05-12 14:21:24.181072 <class 'datetime.datetime'> 前面的datetime是模块名, 后面的datetime是类名
# 虽然打印出来了, 但是他是一个对象, 我们想把他变成字符串

# 将这个对象格式化成字符串
str_time = curr_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(str_time, type(str_time))  # 2023-05-12 14:38:20  # <class 'str'>

# 由于curr_datetime 是一个对象, 我们可以通过属性访问
print(curr_datetime.year)  # 2023
print(curr_datetime.month)  # 5
print(curr_datetime.day)  # 12









