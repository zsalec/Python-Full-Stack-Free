# OOP

# 类的例子
# 注意类的定义
# - 类的属性
# 注意类的定义

'''
# 类的变量作用域的问题
- 类变量：属于类自己的变量
- 实例变量：属于实例的变量
- 访问实例的属性，如果实例没有定义属性，则自动访问类的属性，如果类也没有定义，则报错
'''

class Student:
    # name,age 是类的变量
    # 注意类的变量的定义位置和方法
    # 不需要前缀
    name = 'Alec'
    age = 18

    def say_hi(self):
        print('Love Turing, Love Life')
        print('name: {}, age: {}'.format(self.name, self.age))
        return None


# 实例化
# 作业：中文名能否当做变量名称（可以）
me = Student()
print(me)
me.say_hi()

'''
# self
- self 可以用其他任何名称代替
'''

class Student2:
    name = 'Alec'
    age = 18

    def say_hi(self, n, a):
        self.name = n
        self.age = a
        print('Love Turing, Love Life')
        print('name: {}, age: {}'.format(self.name, self.age))
        return None


tommy = Student2()
print(tommy)
tommy.say_hi('Tommy', 60)


# - 访问类的属性
class Student3:
    name = 'Alec'
    age = 18

    def say_hi(self, n, a):
        self.name = n
        self.age = a
        print('Love Turing, Love Life')
        print('name: {}, age: {}'.format(self.name, self.age))  # name: Jerry, age: 55
        return None

    @staticmethod
    def say_sos():
        print('SOS')
        # - 访问类属性或方法，通过 __class__ 或者 类名称
        # - 不能访问实例的属性
        print('name: {}, age: {}'.format(Student3.name, __class__.age))  # name: Alec, age: 18
        return None


jerry = Student3()
jerry.say_hi('Jerry', 55)
jerry.say_sos()

mickey = Student3()
mickey.say_sos()


# -- 构造函数
class Beast:
    name = 'NonName'
    age = 0

    def __init__(self, name, age):
        print('This is construct function')
        self.name = name
        self.age = age
        return None


rabbit = Beast('Rabbit', 3)
print('-----------------------')
print(rabbit.name)
print(rabbit.age)
