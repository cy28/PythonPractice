p = "Education is the key to unlocking one's full potential and shaping a brighter future. It empowers individuals to acquire knowledge, develop critical thinking skills, and pursue their passions."


punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for i in p:
    if i in punctuation:
        p = p.replace(i, "")  # 将符号用空格代替

print(p)

# Education is the key to unlocking ones full potential and shaping a brighter future It empowers individuals to acquire knowledge ...........

print(type(punctuation))  # <class 'str'>

