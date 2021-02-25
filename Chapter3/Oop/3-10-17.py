# 属性案例
# 创建 Student 类，描述学生类
# 学生具有 Student.name 属性
# 但 name 格式不统一
# 可以用增加一个函数，然后自动调用的方式，但是很蠢
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.setName(name)

    # 介绍自己
    def intro(self):
        print('Hi, my name is {}'.format(self.name))
        return None

    def set_name(self, name):
        self.name = name.upper()
        return None


s1 = Student('Tonny', 19)
s2 = Student('mickey stangle', 24)

s1.intro()
s2.intro()
