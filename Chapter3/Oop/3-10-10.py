# 多继承 Demo
# 子类可以直接拥有父类的属性和方法，私有属性和方法除外
class Fish:
    def __init__(self, name):
        self.name = name
        return None

    def swim(self):
        print('I am swimming.')
        return None


class Bird:
    def __init__(self, name):
        self.name = name
        return None

    def fly(self):
        print('I am flying.')
        return None


class Person:
    def __init__(self, name):
        self.name = name
        return None

    def work(self):
        print('I am working.')
        return None


class SuperMan(Person, Bird, Fish):
    def __init__(self, name):
        self.name = name
        return None


s = SuperMan('Supper Name')
s.fly()
s.swim()
s.work()
'''I am flying.
I am swimming.
I can working.
'''


# 单继承 Demo
class Student(Person):
    def __init__(self, name):
        self.name = name
        return None


stu = Student('yueyue')
stu.work()
'''
I am working.
'''
