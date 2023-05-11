"""
# 将可迭代对象(列表), 通过连接符, 连接成一个字符串

join() 是字符串对象的一个方法，用于将一个可迭代对象中的元素连接成一个字符串。它在每个元素之间插入指定的连接符，并返回连接后的字符串。

join() 方法的语法为：separator.join(iterable)。

separator：表示要插入的连接符，可以是一个字符串或字符。

iterable：表示要连接的可迭代对象，通常是一个列表、元组或字符串等。

"""
fruits = ['apple', 'banana', 'orange']

# 使用逗号连接列表中的元素
result1 = ', '.join(fruits)
print(result1)
# 输出：'apple, banana, orange'

# 使用空格连接字符串中的字符
result2 = ' '.join('Hello')
print(result2)
# 输出：'H e l l o'

# 使用连接符为空字符串，将列表中的元素连接成一个字符串
result3 = ''.join(fruits)
print(result3)
# 输出：'applebananaorange'































