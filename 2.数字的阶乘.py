# 1. 自己写的
def factorial1(n):
    result = 1
    for i in range(n):
        result *= (i + 1)
    print(result)


factorial1(5)  # 120


# 2. 视频中的方法 倒着乘
def factorial2(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1
    print(result)


factorial2(3)  # 6


# 3. 正着乘

def factorial3(n):
    result = 1
    r = 1
    while r <= n:
        result *= r
        r += 1
    print(result)


factorial3(4)  # 24


# 采用递归的方式
def factorial4(n):
    if n == 0 or n == 1:  # 0的阶乘是1 考虑到了这种特殊情况
        return 1
    else:
        return n * factorial4(n - 1)


print(factorial4(6))  # 720


# 当n等于0时，根据阶乘的定义，0的阶乘为1。因此在阶乘函数的实现中，需要单独考虑这种情况，以确保函数的正确性。
# 如果不考虑n等于0的情况，当n为0时，函数将返回None或抛出异常等错误结果，这显然是不符合阶乘定义的。
# 因此，我们需要在函数中进行特判，以确保能够正确处理n等于0的情况。







