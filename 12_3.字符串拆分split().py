"""
# 将字符串根据分割符拆分, 返回由拆分元素构成的一个列表

split() 是 Python 字符串对象的一个方法，用于将字符串按照指定的分隔符进行拆分，并返回一个由拆分后的子字符串组成的列表。

split() 方法的语法为：string.split(sep, maxsplit)。

sep：可选参数，表示要用作分隔符的字符串。默认情况下，sep 的值是空白字符（空格、制表符、换行符等），它将会根据空白字符进行拆分。

maxsplit：可选参数，表示最大拆分次数。如果指定了 maxsplit 参数，字符串将被拆分成 maxsplit + 1 个子字符串。
如果省略了 maxsplit 参数或将其设置为 -1，则不限制拆分次数。

"""

sentence = "Hello, world! How are you?"

# 使用空白字符进行拆分
words = sentence.split()
print(words)
# 输出：['Hello,', 'world!', 'How', 'are', 'you?']

# 使用逗号进行拆分
parts = sentence.split(',')
print(parts)
# 输出：['Hello', ' world! How are you?']

# 限制拆分次数为1
split_once = sentence.split(' ', 1)
print(split_once)
# 输出：['Hello,', 'world! How are you?']


