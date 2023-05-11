"""
在 Python 中，if not 是一个条件语句的结构，用于检查条件是否为 False。它可以用于判断一个表达式的否定结果。

当 if not 后面的条件表达式为 False、None、空容器（如空列表、空字典、空字符串等）或数值零时，条件判断为 True。否则，条件判断为 False。

非0和非空都返回True

就相当于if not + 一个0或空, 就会执行后面的内容

"""

value = 0

if not value:  # 这里value=0, 而非0就是True
    print("Value is zero")  # 因为 value 为零，条件判断为 True，所以打印 "Value is zero"

text = ""

if not text:
    print("Text is empty")  # 因为 text 为空字符串，条件判断为 True，所以打印 "Text is empty"

my_list = []

if not my_list:
    print("List is empty")  # 因为 my_list 为空列表，条件判断为 True，所以打印 "List is empty"

my_dict = {}

if not my_dict:
    print("Dictionary is empty")  # 因为 my_dict 为空字典，条件判断为 True，所以打印 "Dictionary is empty"


















