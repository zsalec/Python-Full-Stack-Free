# demo


class Student():
    name = 'dana'
    age = 18


print(type(Student.__dict__))
print(Student.__dict__)
'''
<class 'mappingproxy'>
{'__module__': '__main__', 'name': 'data', 'age': 18, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
'''
# 实例化
yueyue = Student()
print(type(yueyue))
print(yueyue.__dict__)
print(yueyue.name)
'''
<class '__main__.Student'>
{}
dana
'''


class A():
    name = 'Tonny'
    age = 18

    # 注意 say 的写法，参数有一个 self
    def say(self):
        self.name = 'Jeery'
        self.age = 20
        return None


# 此案例说明
# 此实例的属性和其对象的属性，在不对对象属性赋值的情况下，指向同一个变量
print(A.name)
print(A.age)
print('*' * 20)
print(id(A.name))
print(id(A.age))
print('*' * 20)
a = A()
print(a.name)
print(a.age)
print('*' * 20)
print(id(a.name))
print(id(a.age))
print(A.__dict__)
print(a.__dict__)
a.name = 'William'
a.age = 30
print(a.__dict__)
print('*' * 20)
print(id(a.name))
print(id(a.age))
'''
Tonny
18
********************
31250160
8790950441760
********************
Tonny
18
********************
31250160
8790950441760
{'__module__': '__main__', 'name': 'Tonny', 'age': 18, 'say': <function A.say at 0x00000000024B4438>, '__dict__': <attribute '__dict__' of 'A' objects>, '__weakref__': <attribute '__weakref__' of 'A' objects>, '__doc__': None}
{}
{'name': 'William', 'age': 30}
********************
36590448
8790950442144
'''


class Student1():
    name = 'dana'
    age = 18

    def say(self):
        self.name = 'William'
        self.age = 20
        print('My name is {}, my age is {}'.format(self.name, self.age))
        return None

    def say_again(s):
        print('My name is {}, my age is {}'.format(s.name, s.age))
        return None


print('*' * 20)
yueyue = Student1()
yueyue.say()
yueyue.say_again()
'''
********************
My name is William, my age is 20
My name is William, my age is 20
'''


class Teacher():
    name = 'Tonny'
    age = 19

    def say(self):
        self.name = 'William'
        self.age = 20
        print('My name is {}, my age is {}'.format(self.name, self.age))
        return None

    @staticmethod
    def say_again():
        print('Hello, nice to see you again!')
        print('My name is {}, my age is {}'.format(__class__.name, __class__.age))
        return None


t = Teacher()
t.say()
# 调用绑定类函数使用类名
Teacher.say_again()
'''
My name is William, my age is 20
Hello, nice to see you again!
My name is Tonny, my age is 19
'''


# 关于 self 案例
class A1():
    name = 'liuying'
    age = 18

    def __init__(self):
        self.name = 'a ha'
        self.age = 20
        return None

    def say(self):
        print('My name is {}, my age is {}'.format(self.name, self.age))
        return None


class B():
    name = 'bbbb'
    age = 90


a = A1()
# 此时，系统会默认把 a 作为第一个参数传入函数
a.say()

# 此时，self 被 a 代替
A1.say(a)
# 同样可以把 A 作为参数传入
A1.say(A)
# 此时，传入的是实例B，因为 B 具有 name 和 age 属性，所以不会报错
A1.say(B)
# 以上代码，利用了鸭子模型
'''
My name is a ha, my age is 20
My name is a ha, my age is 20
My name is Tonny, my age is 18
My name is bbbb, my age is 90
'''


# 私有变量案例
class Person():
    # name 是共有的成员
    name = 'liuying'
    # __age 就是私有成员
    __age = 19


p = Person()
# name 是公有变量
print(p.name)
# __age 是私有变量
try:
    print(p.__age)
except AttributeError:
    print("AttributeError: 'Person' object has no attribute '__age'")
print(Person.__dict__)
p._Person__age = 30
print(p._Person__age)
'''
liuying
AttributeError: 'Person' object has no attribute '__age'
{'__module__': '__main__', 'name': 'liuying', '_Person__age': 19, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
30
'''
