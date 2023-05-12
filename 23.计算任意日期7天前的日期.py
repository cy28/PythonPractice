import datetime


# 封装一个函数, 传入一个日期字符串和间隔的天数
def get_diff_days(pdate, days):
    # 现将传入的日期字符串转化为对象
    pdate_obj = datetime.datetime.strptime(pdate, '%Y-%m-%d')
    # 创建一个日期间隔对象
    time_gap = datetime.timedelta(days=days)
    # 得到间隔后的日期对象
    pdate_result = pdate_obj - time_gap
    # 返回一个字符串
    return pdate_result.strftime('%Y-%m-%d')


print(get_diff_days('2023-5-12', 1))  # 2023-05-11
print(get_diff_days('2023-5-12', 3))  # 2023-05-09
print(get_diff_days('2023-5-12', 5))  # 2023-05-07
































