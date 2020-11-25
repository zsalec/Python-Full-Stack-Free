# 继承中的构造函数 #2
class Animal:
    pass


class Reptile(Animal):
    pass


class Mammal(Animal):
    def __init__(self):
        print('Mammal')
        return None


class Dog(Mammal):
    def __init__(self):
        print('I am init in Dog class')
        return None


# 实例化的时候，括号的参数需要跟构造函数参数匹配
kaka = Dog()  # I am init in Dog class


# Cat 没有写构造函数
class Cat(Mammal):
    pass


# 此时应该自动调用父类的构造函数
# 在 Mammal 中查找到了构造函数，则停止向上查找
c = Cat()  # Mammal
