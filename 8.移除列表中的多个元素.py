"""
输入:
    原始元素: [3, 5, 7, 9, 11, 13]
    移除元素: [7, 11]
返回:
    [3, 5, 9, 13]

"""

# 1. 使用列表推导式来完成

original_list = [3, 5, 7, 9, 11, 13]
remove_list = [7, 11]

new_list = [x for x in original_list if x not in remove_list]

print(new_list)  # 输出 [3, 5, 9, 13]


# 2. 定义一个函数来完成

list1 = [3, 5, 7, 9, 11, 13]
list2 = [7, 11]


# 传入原始列表和要去除的列表, 遍历要去除的列表, 得到一个一个元素, 然后在原始列表中去除这些元素

def new_list1(ori, rem):
    for i in rem:
        ori.remove(i)
        n_list = ori
    print(n_list)


new_list1(list1, list2)  # 输出 [3, 5, 9, 13]

























