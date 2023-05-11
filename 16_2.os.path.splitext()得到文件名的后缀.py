# splitext 是 "split extension" 的缩写。

"""
函数签名如下：

os.path.splitext(path)
参数 path 是要进行分割的文件路径。

splitext 函数会将文件路径分割成两部分，即文件名和扩展名，并以元组的形式返回。如果路径中没有扩展名，则返回的元组的第二个元素是空字符串。

"""

import os

path1 = '/path/to/file.txt'

f = os.path.splitext(path1)

name1, ext1 = os.path.splitext(path1)

print(f)      # 输出: ('/path/to/file', '.txt')  返回的是一个元组
print(name1)  # 输出: /path/to/file
print(ext1)   # 输出: .txt










