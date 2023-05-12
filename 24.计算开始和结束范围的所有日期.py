"""
输入:
    开始日期 2021-4-28
    结束日期 2021-05-03
输出:
[ 2021-4-28, 2021-4-29, 2021-4-30, 2021-05-01, 2021-05-02, 2021-05-03 ]

知识点:
    1. 怎么给日期加一天
    2. 怎样比较两个日期

"""

from datetime import datetime, timedelta


def generate_date_range(start_date_str, end_date_str):

    # 创建时间对象
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

    date_list = []

    while start_date <= end_date:
        # 将时间对象改成字符串, 然后写入列表
        date_list.append(start_date.strftime('%Y-%m-%d'))
        start_date += timedelta(days=1)

    return date_list


# 测试函数
start_date = '2021-04-28'
end_date = '2021-05-03'
result = generate_date_range(start_date, end_date)
print(result)
















