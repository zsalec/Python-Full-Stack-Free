# 继承中的构造函数 #1
class Animal:
    pass


class Reptile(Animal):
    pass


class Mammal(Animal):
    pass


class Dog(Mammal):
    def __init__(self):
        print('I am init in Dog class')


# 实例化的时候，括号的参数需要跟构造函数参数匹配
kaka = Dog()
