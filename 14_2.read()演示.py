filename = 'English article14'


with open(filename, 'r') as file:
    content = file.read()

print(content)

print(type(content))  # <class 'str'>
