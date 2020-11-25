# 继承中的构造函数 #3
class Animal:
    pass


class Reptile(Animal):
    pass


class Mammal(Animal):
    def __init__(self, name):
        print('Mammal {}'.format(name))
        return None


class Dog(Mammal):
    def __init__(self):
        print('I am init in Dog class')
        return None


# 实例化 Dog 的时候，查找到 Dog 的构造函数，参数匹配，不报错
kaka = Dog()  # I am init in Dog class


# Cat 没有写构造函数
class Cat(Mammal):
    pass


# 此时应该自动调用父类的构造函数
# 在 Mammal 中查找到了构造函数，则停止向上查找
# 参数不匹配时，抛出 TypeError 异常
try:
    c = Cat()  # Mammal
except TypeError:
    print("TypeError: __init__() missing 1 required positional argument: 'name'")
