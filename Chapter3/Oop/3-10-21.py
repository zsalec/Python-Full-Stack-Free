# 抽象
class Animal:
    def sayHello(self):
        pass


class Dog(Animal):
    def sayHello(self):
        print('问一下对方')
        return None


class Person(Animal):
    def sayHello(self):
        print('Kiss me')
        return None


d = Dog()
d.sayHello()
p = Person()
p.sayHello()
'''
问一下对方
Kiss me
'''
