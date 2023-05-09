numbers = [11, 11, 20, 12, 1, 14, 19, 11]

# 1. 原地排序, 将原列表进行改变, 默认是升序

# sort()  将列表中的数字从小到大排列, 默认是升序, 不会生成新列表
numbers.sort()
print(numbers)  # [1, 11, 11, 11, 12, 14, 19, 20]

# reverse=True  降序排列
numbers.sort(reverse=True)
print(numbers)  # [20, 19, 14, 12, 11, 11, 11, 1]


# 2. 返回一个新列表
# sorted() 会把排序后的结果生成一个新列表，传入的参数是原列表
list1 = [12, 34, 21, 35, 6, 24]

list2 = sorted(list1)  # 默认是升序排列
print(list2)  # [6, 12, 21, 24, 34, 35]

































