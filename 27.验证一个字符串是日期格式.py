# 日期格式: YYYY-MM-DD

import re


def is_valid_date(date_string):
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(pattern, date_string):
        return True
    else:
        return False


# 测试示例
dates = ["2022-01-01", "2022-12-31", "2022-13-01", "2022/01/01", "22-01-01", "2022-1-1"]

for date in dates:
    if is_valid_date(date):
        print(f"{date} is a valid date")
    else:
        print(f"{date} is not a valid date")
























