import datetime

# 1. 将文件中的数据放在一个字典中
sales_list = {}

with open('日期销售数据26.txt', 'r') as file:
    for line in file:
        line = line.strip()  # 去除行首尾的空格和换行符
        date, sale_number = line.split(': ')  # 按': '分割行，得到一个列表
        sales_list[date] = float(sale_number)  # 注意这里要把数据转化为浮点型

print(sales_list)


# 2. 写一个函数计算一个日期7天前的日期
def get_diff_days(pdate):
    # 现将传入的日期字符串转化为对象
    pdate_obj = datetime.datetime.strptime(pdate, '%Y-%m-%d')
    # 创建一个日期间隔对象
    time_gap = datetime.timedelta(days=7)
    # 得到间隔后的日期对象
    pdate_result = pdate_obj - time_gap
    # 返回一个字符串
    return pdate_result.strftime('%Y-%m-%d')


# 计算周同比
for date, sale_number in sales_list.items():
    # 得到每个日期七天前的日期
    date_before7 = get_diff_days(date)
    # 得到七天前的销售额
    sale_number_before7 = sales_list.get(date_before7, 0)  # 如果不存在, 返回默认值0
    if sale_number_before7 == 0:
        print(date, sale_number, 0)
    else:
        week_diff = (sale_number - sale_number_before7) / sale_number_before7
        print(date, sale_number, date_before7, sale_number_before7, week_diff)



















