# 输入开始数字和结束数字, 打印该区间中所有的素数

# 判断是否是素数的函数
def is_prime(n):
    if n in (1, 2):
        # (1, 2) 是一个元组，它里面包含了两个元素 1 和 2。
        # n 是要进行判断的对象，in 表示判断 n 是否在元组 (1, 2) 中。所以 n 只能取到 1 或 2 才能使 if 条件成立。
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    else:  # for循环被全部遍历完, 执行else语句
        return True


# 打印区间的素数
def print_prime(start, end):
    list1 = []
    for i in range(start, end+1):
        if is_prime(i):
            list1.append(i)
    print(list1)


print_prime(1, 10)































