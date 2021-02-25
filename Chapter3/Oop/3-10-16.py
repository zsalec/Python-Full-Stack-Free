# Mixin Demo
class Person:
    name = 'Alec'
    age = 18

    def eat(self):
        print('EAT......')
        return None

    def drink(self):
        print('DRINK.......')
        return None

    def sleep(self):
        print('SLEEP......')
        return None


class Teacher(Person):
    def work(self):
        print('Work...')
        return None


class Student(Person):
    def study(self):
        print('Study...')
        return None


class Tutor(Teacher, Student):
    pass


t = Tutor()

print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__)
'''
(<class '__main__.Tutor'>, <class '__main__.Teacher'>, <class '__main__.Student'>, <class '__main__.Person'>, <class 'object'>)
{}
{'__module__': '__main__', '__doc__': None}
'''

print('*' * 20)


class TeacherMixin:
    def work(self):
        print('WORK......')
        return None


class StudentMixin:
    def study(self):
        print('STUDY......')
        return None


class TutorM(Person, TeacherMixin, StudentMixin):
    pass


tt = TutorM()
print(TutorM.__mro__)
print(tt.__dict__)
print(TutorM.__dict__)
'''
(<class '__main__.TutorM'>, <class '__main__.Person'>, <class '__main__.TeacherMixin'>, <class '__main__.StudentMixin'>, <class 'object'>)
{}
{'__module__': '__main__', '__doc__': None}
'''


# - issubclass
class A:
    pass


class B(A):
    pass


class C:
    pass


print('issubclass(B, A):', issubclass(B, A))
print('issubclass(C, A):', issubclass(C, A))
print('issubclass(C, object):', issubclass(B, object))
'''
issubclass(B, A): True
issubclass(C, A): False
issubclass(C, object): True
'''

# - isinstance
a = B()
print('isinstance(a, A)', isinstance(a, A))
print('isinstance(a, B)', isinstance(a, B))
print('isinstance(a, C)', isinstance(a, C))
'''
isinstance(a, A) True
isinstance(a, B) True
isinstance(a, C) False
'''


# -hasattr
class D:
    name = 'NoName'


d = D()
print('hasattr(d, "name"):', hasattr(d, 'name'))
print('hasattr(d, "age"):', hasattr(d, 'age'))
'''
hasattr(d, "name"): True
hasattr(d, "age"): False
'''

# help 案例
help(setattr)
'''
Help on built-in function setattr in module builtins:

setattr(obj, name, value, /)
    Sets the named attribute on the given object to the specified value.
    
    setattr(x, 'y', v) is equivalent to ``x.y = v''
'''

# dir 案例
print(dir(A))
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
'''
a = A()
print(dir(a))
'''
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
'''
help(dir)
'''
Help on built-in function dir in module builtins:

dir(...)
    dir([object]) -> list of strings
    
    If called without an argument, return the names in the current scope.
    Else, return an alphabetized list of names comprising (some of) the attributes
    of the given object, and of attributes reachable from it.
    If the object supplies a method named __dir__, it will be used; otherwise
    the default dir() logic is used and returns:
      for a module object: the module's attributes.
      for a class object:  its attributes, and recursively the attributes
        of its bases.
      for any other object: its attributes, its class's attributes, and
        recursively the attributes of its class's base classes.
'''