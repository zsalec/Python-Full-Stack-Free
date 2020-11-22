# OOP

# - 类的属性
class Student:
    name = 'Alec'
    age = 18

    def say_hi(self):
        print('Love Turing, Love Life')
        print('name: {}, age: {}'.format(self.name, self.age))
        return None


me = Student()
print(me)
me.say_hi()


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
