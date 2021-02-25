# 包含一个学生类
# 一个 sayHello 函数
# 一个打印语句
class Student:
    def __init__(self, name='NoName', age=18):
        self.name = name
        self.age = age

    def say(self):
        print('My name is {}'.format(self.name))
        return None


def say_hello():
    print('Hi, welcome python')
    return None


if __name__ == 'main':
    print('I am is 01 module')
