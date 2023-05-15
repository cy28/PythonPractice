"""
写一个函数, 验证密码是否满足条件
1. 长度位于[6-12]之间
2. 必须包含至少一个小写字母
3. 必须包含至少一个大写字母
4. 必须包含至少一个数字
5. 必须包含至少一个特殊字符
"""

import re


def validate_password(password):
    # 检查密码长度
    if len(password) < 6 or len(password) > 12:
        return False, '长度必须位于[6-12]之间'

    # 检查是否包含小写字母
    if not re.search(r'[a-z]', password):
        return False, '必须包含至少一个小写字母'

    # 检查是否包含大写字母
    if not re.search(r'[A-Z]', password):
        return False, '必须包含至少一个大写字母'

    # 检查是否包含数字
    if not re.search(r'\d', password):
        return False, '必须包含至少一个数字'

    # 检查是否包含特殊字符
    # if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
    if not re.search(r'[^0-9A-Za-z]', password):
        return False, '必须包含至少一个特殊字符'

    # 所有条件都满足
    return True


# 测试示例密码
passwords = ["Abcdef12!", "abc123", "ABCDEFGH", "abc!@#123", "abc123", "abcdefghi123", "Abcdefgh!"]

for password in passwords:
    print(password,validate_password(password))




































