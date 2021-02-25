# 面向对象的三大特征
# - 继承
# - 封装
# - 多态


# - 继承
# -- 父类（supperClass, baseClass)
# -- 所有的类必须有父类，允许有多个，默认的父类是 object
class Person:
    name = 'NonName'
    age = 0


class Person2(object):
    pass


class Teacher(Person):
    pass


t = Teacher()
print(t.name)  # NonName


class Bird:
    fly = 'Yes, I can fly'

    def flying(self):
        print(self.fly)
        print('flying, flying...')


class BirdMan(Person, Bird):
    pass


bm = BirdMan()
bm.flying()
'''
Yes, I can fly
flying, flying...
'''
print(bm.fly)  # Yes, I can fly


class Teacher(Person):
    pass


# -- 检测是否为子类 issubclass
print(issubclass(BirdMan, Person))  # True
print(issubclass(BirdMan, Bird))  # True
print(issubclass(BirdMan, Teacher))  # False

help(issubclass)


# - 构造函数
# -- 在实例化时调用的第一个函数
# -- 自动调用
# -- 要求：第一个参数必须有，一般推荐 self
# -- 不能有返回值，只能返回None。 return None
class Person4:
    name = 'NonName'
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('name: {}, age {}'.format(name, age))
        print('**************')
        return None


p = Person4('White', 3)
print('====================')
print('name: {}, age: {}'.format(p.name, p.age))  # name: White, age: 3


class Teacher1(Person4):
    def __init__(self, name, age):
        super(Teacher1, self).__init__(name, age)
        print('-----------')
        return None


t = Teacher1('Bill', 77)
'''
name: White, age: 3
name: Bill, age 77
**************
-----------
'''
print('==============')
print('[outside] name: {}, age: {}'.format(t.name, t.age))  # [outside] name: Bill, age: 77
