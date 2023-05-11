# strip() 是 Python 字符串方法之一，用于去除字符串的首尾空白字符（包括空格、制表符和换行符）。
# strip() 方法返回一个新的字符串，其中移除了原始字符串开头和结尾的空白字符。如果原始字符串内部存在空白字符，它们不会被移除。


with open('grade_list17', 'r', encoding='utf-8') as fin:

    for line in fin:
        line = line.strip()
        print(line)
















