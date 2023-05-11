# 统计每个单词的出现次数
"""
word_count = {}  # 将每个单词出现的次数存在一个字典中

with open('English article14') as f_in:
    for line in f_in:
        line = line[:-1]                # 去掉换行符
        words = line.split()            # 每一行以空格为分隔符, 得到一个小列表
        for word in words:              # 遍历这个小列表
            if word not in word_count:
                word_count[word] = 0    # 不在将键值设为0
            word_count[word] += 1       # 在值加1

print(word_count)  # 这样写有一个问题, 符号没有去掉

"""


filename = 'English article14'

# Read the content of the file
with open(filename, 'r') as file:
    content = file.read()  # 是一个装了整个文章的大字符串

# Convert the content to lowercase to ignore case sensitivity
content = content.lower()  # 将整个字符串的字母字符全部转小写, 忽略大小写的影响

# Remove punctuation marks
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for char in content:
    if char in punctuation:
        content = content.replace(char, "")  # 将符号用空格代替

# Split the content into individual words
words = content.split()  # 以空格将每个单词分割成一个小列表, 并返回一个大列表

# Count the occurrence of each word
dict1 = {}  # 建立一个字典
for word in words:
    if word in dict1:
        dict1[word] += 1  # word就是每一个单词, 作为键
    else:
        dict1[word] = 1

# Print the word count
for word, count in word_count.items():
    print(f"{word}: {count}")



"""

# 问题: words = content.split()为什么要进行这一步, 不直接用content

答:
    当我们处理文本数据时，经常需要按照单词进行操作和分析。通过使用 split() 方法，我们可以将字符串按照默认的空格字符进行分割，从而得到一个包含各个单词的列表。

如果直接使用 content 字符串进行操作，例如遍历字符串的每个字符，那么无法准确地获取单词的信息，因为单词之间没有明确的分隔符。通过将字符串拆分成单词列表，我们可以更方便地对每个单词进行处理，例如计数、查找特定单词等操作。

因此，将字符串 content 使用 split() 方法拆分成单词列表 words 可以更好地处理和操作文本数据。


也就是说. 如果使用content会遍历字符而不是单词


"""














