import datetime

# 1. 给定一个日期字符串
birthday = "1997-12-20"

# 2. 将字符串改成一个datetime.datetime对象
# .strptime(时间字符串, 给的这个字符串的时间格式)  -string phrase time
birthday_date = datetime.datetime.strptime(birthday, '%Y-%m-%d')

print(birthday_date, type(birthday_date))  # 1997-12-20 00:00:00 <class 'datetime.datetime'>

# 3. 当前时间
curr_datetime = datetime.datetime.now()

# 4. 计算差值, 得到的是 'datetime.timedelta'对象
minus_datetime = curr_datetime - birthday_date
print(minus_datetime, type(minus_datetime))
# 9274 days, 14:54:45.213864 <class 'datetime.timedelta'>










