# 1. 把成绩整合放在一个字典中, 键就是学科, 值就是由分数构成的列表
course_grade = {}


with open('grade_list17', 'r', encoding='utf-8') as fin:
    # 读取每一行
    for line in fin:
        # 去掉行尾的换行符
        # line = line[:-1]
        line = line.strip()
        number, name, course, grade = line.split(' ')
        # 键不在字典中, 就创建该键
        if course not in course_grade:
            course_grade[course] = []
        course_grade[course].append(int(grade))

print(course_grade)

for course, grades in course_grade.items():
    print(course, max(grades), min(grades), sum(grades)/len(grades))

























