"""
输入文件:
    三列: 学号 姓名 成绩
    列之间用逗号隔开, 比如101, 小张, 88
    行之间用\n分割
输出:
    最高分 最低分 平均分
"""

# 仍然沿用第12个问题的student_grade12


def compute_score(file):
    scores = []  # 计划把所有学生的成绩读到这个score中
    # 1. 开始读这个学生成绩文件
    with open(file) as f_in:
        # 2. 遍历文件的每一行
        for i in f_in:
            # 3. 将字符串切片, 不要每一行的换行符
            i = i[:-1]
            # 4. 将每一行字符串, 以逗号拆分, 得到一个小列表
            ele = i.split(',')
            # 5. 将这个小列表中的最后一位元素, 存到scores中
            scores.append(int(ele[-1]))
        # 6. 得到score列表的最大值
        max_score = max(scores)
        # 7. 得到最小值
        min_score = min(scores)
        # 8. 得到平均值
        ave_score = sum(scores) / len(scores)
        print(f'成绩的最大值是{max_score}, 最小值是{min_score}, 平均值是{ave_score}')


compute_score('student_grade12')
# 成绩的最大值是99, 最小值是44, 平均值是71.5



















