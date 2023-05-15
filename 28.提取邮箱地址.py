import re

content = """
当我登录到我的电子邮箱时，我惊喜地发现了一封来自不同人的邮件。我打开第一封邮件，发现发件人是mysterious82@email.com，他提到了一个令人兴奋的项目合作机会。我迫不及待地回复了这封邮件，分享了我的兴趣和相关经验。

接着，我点击第二封邮件，发现发件人是adventureseeker76@gmail.com。他描述了一个令人心动的旅行计划，邀请我加入他们的探险团队。我立即回复了邮件，表达了我对这次冒险的热情，并询问了更多细节。

最后，我打开了第三封邮件，发现发件人是creativeartist99@hotmail.com。她分享了她最新的艺术作品，并希望能与我合作展示。我感到非常荣幸，并迅速回复了这封邮件，表达了我对她的创作的赞赏，并提出了一些合作想法。

这一切让我感到兴奋不已，我迫不及待地回复了这些邮件，并期待着未来的合作和冒险。
"""


def extract_emails(content):
    # 开头 字母数字下划线和中横线  [\w-]+
    # 中间 @
    # 后面 字母数字下划线  [A-Za-z0-9]+
    # 加上一点 .  \.
    # 最后 两位以上字母  [A-Za-z]{2,}

    # 由于\w相当于[A-Za-z0-9_]但是也可以匹配中文, 所以还是直接写比较好
    email_regex = r'[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Za-z]{2,4}'
    emails = re.findall(email_regex, content)
    return emails


# 提取邮箱地址
emails = extract_emails(content)
print(emails)

# 打印提取的邮箱地址
for email in emails:
    print(email)











