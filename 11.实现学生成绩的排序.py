"""
学生成绩的数据格式:
    复杂列表: 元素是字典或者元组
    [
    {'no': 101, 'name': '小张', 'grade': 88},
    {'no': 102, 'name': '小王', 'grade': 77},
    {'no': 103, 'name': '小李', 'grade': 99},
    {'no': 104, 'name': '小赵', 'grade': 66}
    ]

"""

students = [
    {'number': 101, 'name': '小张', 'grade': 88},
    {'number': 102, 'name': '小王', 'grade': 77},
    {'number': 103, 'name': '小李', 'grade': 99},
    {'number': 104, 'name': '小赵', 'grade': 66}
]

# 匿名函数的语法如下：
# lambda arguments: expression
# 注意:
#     1. arguments 是匿名函数的参数列表，用逗号分隔。在上面的示例中，参数列表只有一个参数 x。
#     2. expression 是匿名函数的返回值。在上面的示例中，返回值是 x * 2。


sorted_students = sorted(students, key=lambda x: x['grade'], reverse=True)

for student in sorted_students:
    print(student)


# 输出
# {'no': 103, 'name': '小李', 'grade': 99}
# {'no': 101, 'name': '小张', 'grade': 88}
# {'no': 102, 'name': '小王', 'grade': 77}
# {'no': 104, 'name': '小赵', 'grade': 66}










