"""
1.
shutil 是 "shell utilities" 的缩写。

shutil 是 Python 标准库中的一个模块，用于提供一些高级的文件和目录操作函数，以便在 Python 程序中执行各种 shell（命令行）相关的操作。

该模块提供了一组函数，用于复制、移动、删除文件和目录，以及处理文件和目录的压缩和归档操作。它还包括一些用于获取文件和目录信息的函数，以及一些其他实用功能。

"""

"""
2. 
"shell utilities" 的中文意思是 "Shell 工具"。

"shell" 是指计算机操作系统提供的一种用户界面，允许用户与操作系统进行交互并执行各种命令。
在大多数操作系统中，包括 Linux、Unix 和 macOS，都提供了命令行界面（即 shell），用户可以通过输入命令和参数来执行各种任务。

"utilities" 指的是实用程序或工具，它们是为了完成特定任务而开发的软件程序。
在计算机科学领域，实用程序通常是一些小型、独立的程序，用于执行特定的功能或解决特定的问题。

因此，"shell utilities" 可以理解为与 shell（命令行界面）相关的实用程序或工具。
这些工具通常用于在命令行环境中执行文件和目录操作、系统管理、文件压缩和归档等任务。
Python 中的 shutil 模块提供了一组这样的实用程序函数，用于简化和执行这些常见的 shell 操作。

"""


"""
shutil.move 是 Python 标准库中 shutil 模块提供的一个函数，用于移动文件或目录。

函数签名如下：

shutil.move(src, dst, copy_function=copy2)
参数 src 是源文件或目录的路径，而参数 dst 是目标位置的路径。

shutil.move 函数的作用是将源文件或目录从 src 移动到 dst，并返回目标位置的路径。如果目标位置已经存在同名文件或目录，将会被覆盖。

默认情况下，shutil.move 使用 copy2 函数来复制文件的内容和元数据（如权限、时间戳等）。
如果希望使用不同的复制函数，可以通过可选参数 copy_function 指定

"""


# 示例

import shutil

# 移动文件
src_file = '/path/to/source/file.txt'
dst_file = '/path/to/destination/file.txt'

shutil.move(src_file, dst_file)

# 移动目录
src_dir = '/path/to/source/directory'
dst_dir = '/path/to/destination/directory'

shutil.move(src_dir, dst_dir)





















