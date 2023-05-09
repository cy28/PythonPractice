
"""
输入包含重复元素的原始列表:
[10, 20, 30, 10, 20]

返回:
[10, 20, 30]
"""

# 要从一个包含重复元素的列表中获取所有唯一元素，可以使用 Python 中的集合（set）数据类型。
# 集合是一个无序、不重复的元素集合，可以通过将原始列表转换为集合来自动去重。
# 然后，我们可以将集合转换回列表，以获取所有唯一元素


# 1. 利用集合进行去重
original_list = [10, 20, 30, 10, 20]
unique_list = list(set(original_list))
print(unique_list)  # 输出 [10, 20, 30]


# 2. 写一个函数进行去重
# 新建一个列表, 将原始列表中的元素添加到这个新列表, 只要元素还不存在于新列表, 就添加到新列表
def get_unique(ori):
    uni = []
    for i in ori:
        if i not in uni:
            uni.append(i)
    print(uni)


get_unique(original_list)  # 输出 [10, 20, 30]




















