# __init__ 举例
class A:
    def __init__(self, name=0):
        print('哈哈，我被调用了')


a = A()  # 哈哈，我被调用了

print('*' * 20)


# __call__ 举例
class B:
    def __init__(self):
        print('哈哈，我被调用了')

    def __call__(self, *args, **kwargs):
        print('我被调用了',)


b = B()
b()
'''
********************
哈哈，我被调用了
我被调用了
'''


# __str__  序列化输出
class C:
    def __init__(self):
        print('哈哈，我被调用了')

    def __call__(self, *args, **kwargs):
        print('我被调用了',)

    def __str__(self):
        return '__str__ 实例'


c = C()
print('c:', c)


# __getattr__ demo
class D:
    name = 'NoName'
    age = 18

    def __getattr__(self, item):
        print('Not found')
        return None


d = D()
print('d.name:', d.name)
print('d.addr:', d.addr)
'''
Not found
None
'''

# __setattr__ 案例
class Person:
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        print('设置属性：{}'.format(key))
        # 下面语句会导致问题，死循环
        #self.key = value
        # 此种情况，为了死循环，规定统一调用父类魔法函数
        super(Person, self).__setattr__(key, value)
        return None


p = Person()
print('p.__dict__:', p.__dict__)
p.age = 18
print('p.__dict__:', p.__dict__)


# __gt__ 案例
class Student:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name

    def __gt__(self, obj):
        print('哈哈，{} 会比 {} 大妈？'.format(self, obj))
        return self._name > obj._name


stu1 = Student('one')
stu2 = Student('two')
print(stu1 > stu2)


# 三种方法的案例
class Animal:
    # 实例方法
    def eat(self):
        print(self)
        print('Eating......')
        return None

    # 类方法
    # 类方法的第一个参数，一般命名为cls，区别于 self
    @classmethod
    def play(cls):
        print(cls)
        print('Playing......')
        return None

    # 静态方法
    # 不需要用第一个参数表示自身或者类
    @staticmethod
    def say():
        print('Saying......')
        return None


dog = Animal()
print('实例方法')
dog.eat()
print('类方法')
Animal.play()
dog.play()
print('静态方法')
Animal.say()
dog.say()
'''
实例方法
<__main__.Animal object at 0x00000000025A0CC8>
Eating......
类方法
<class '__main__.Animal'>
Playing......
<class '__main__.Animal'>
Playing......
静态方法
Saying......
Saying......
'''
