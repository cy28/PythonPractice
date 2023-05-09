# 输入一个开始的值, 再输入一个结束的值(不包括), 得到所有的偶数, 返回一个列表

# def print_even():
#     start = int(input('请输入区间的开始值: '))
#     end = int(input('请输入区间的结束值: '))
#     list1 = []
#     for i in range(start, end):
#         if i % 2 == 0:
#             list1.append(i)
#     print(list1)
#
# 
# print_even()


# 也可以直接用列表推导式来完成

def print_even1():
    start = int(input('请输入区间的开始值: '))
    end = int(input('请输入区间的结束值: '))
    list1 = [i for i in range(start, end) if i % 2 == 0]
    print(list1)

print_even1()





















