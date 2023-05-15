# content = """
# 小明上街买菜
# 买了1斤黄瓜花了8元
# 买了2斤葡萄花了13.5元
# 买了3斤白菜花了5.4元
# """
# 要求提取(1 黄瓜 8), (2 葡萄 13.5), (3 白菜 5.4)

import re


def extract_shopping_records(text):
    records = []
    pattern = r"买了(\d+)斤(\S+)花了([\d.]+)元"
    # \S：匹配任何非空白字符（不包括空格、制表符、换行符等）
    # [\d.]+ 可以用于匹配一个或多个连续的数字或小数点
    matches = re.findall(pattern, text)
    print(matches)

    for match in matches:
        quantity = match[0]
        item = match[1]
        cost = match[2]
        records.append((quantity, item, cost))

    return records


# 测试提取购买记录并打印
content = """
小明上街买菜
买了1斤黄瓜花了8元
买了2斤葡萄花了13.5元
买了3斤白菜花了5.4元
"""

records = extract_shopping_records(content)

for record in records:
    print(f"({record[0]} {record[1]} {record[2]})")


# [('1', '黄瓜', '8'), ('2', '葡萄', '13.5'), ('3', '白菜', '5.4')]
# (1 黄瓜 8)
# (2 葡萄 13.5)
# (3 白菜 5.4)






