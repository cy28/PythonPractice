# 在Python中，一个对象本身并不具备返回值。对象是对数据和方法的抽象，用于表示和操作特定类型的数据。
# 然而，可以通过在对象中定义方法，并在方法中使用return语句来使对象具有返回值。


# 方法一 定义一个函数, 使的对象有返回值
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width


# 创建一个矩形对象
rectangle = Rectangle(5, 3)

# 直接打印对象名  会返回对象的地址
print(rectangle)  # <__main__.Rectangle object at 0x000001EC1023FD00>

# 调用对象的方法，并获取返回值
area = rectangle.calculate_area()
print("矩形的面积:", area)


# 方法二 用__str__方法定制输出

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


# 创建一个Person对象
person = Person("Alice", 30)

# 打印Person对象
print(person)  # Person(name=Alice, age=30)

























