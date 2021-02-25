# property 案例
# 定义一个 Person 类，具有 name，age 属性
# 对于任意输入的姓名，我们希望都用大写方式保存
# 对于年龄，我们希望内部同一用整数保存
# x = property(fget, fset, fdel, doc)
class Person:
    '''
    这是一个人，一个高尚的人，一个脱离低级趣味的人
    他还有属性
    '''

    _name = ''

    # 函数的名称可以任意
    def fget(self):
        return self._name * 2

    def fset(self, name):
        # 所有输入的姓名一大些形式保存
        self._name = name.upper()
        return None

    def fdel(self):
        self._name = 'NoName'
        return None

    name = property(fget, fset, fdel, '对 name 进行下下操作啦')

    _age = 18

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = int(age)
        if self._age < 0:
            self._age = 0
        return None

    def del_age(self):
        self._age = 18
        return None

    age = property(get_age, set_age, del_age, '对 age 操作')


p1 = Person()
p1.name = 'Turing'
print('p1.name:', p1.name)  # TURINGTURING
p1.age = 18.8
print('p1.age:', p1.age)

# 类的内置属性
print('Person.__dict__:', Person.__dict__)
print('Person.__doc__:', Person.__doc__)
print('Person.__name__:', Person.__name__)
print('Person.__bases__:', Person.__bases__)
'''
Person.__dict__: {'__module__': '__main__', '__doc__': '\n    这是一个人，一个高尚的人，一个脱离低级趣味的人\n    他还有属性\n    ', '_name': '', 'fget': <function Person.fget at 0x0000000001F2CEE8>, 'fset': <function Person.fset at 0x0000000001F2CCA8>, 'fdel': <function Person.fdel at 0x000000000238A678>, 'name': <property object at 0x0000000001F21D18>, '_age': 18, 'get_age': <function Person.get_age at 0x00000000023904C8>, 'set_age': <function Person.set_age at 0x0000000002390EE8>, 'del_age': <function Person.del_age at 0x00000000023808B8>, 'age': <property object at 0x0000000002316098>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>}
Person.__doc__: 
    这是一个人，一个高尚的人，一个脱离低级趣味的人
    他还有属性

Person.__name__: Person
Person.__bases__: (<class 'object'>,)
'''
