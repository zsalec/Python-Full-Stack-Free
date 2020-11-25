# 继承的语法
# 在 Python 中，任何类都有一个共同的父类 object
class Person:
    name = 'NoName'
    age = 0
    __score = 0  # 考试成绩是秘密，只有自己知道
    _petname = 'sec'  # 小名，是受保护的，子类可以用，单不能公用

    def sleep(self):
        print('Sleeping......')
        return None


# 父类卸载括号中
class Teacher(Person):
    teacher_id = '9527'
    name = 'dana'

    def make_test(self):
        print('attention')
        pass


t = Teacher()
print('t.Name:', t.name)
print('Teacher.name:', Teacher.name)
print('t._petname:', t._petname)
try:
    print('t.__score:', t.__score)
except AttributeError:
    print("AttributeError: 'Teacher' object has no attribute '__score'")
t.sleep()
print('t.teacher_id:', t.teacher_id)
t.make_test()
'''
t.Name: dana
Teacher.name: dana
t._petname: sec
AttributeError: 'Teacher' object has no attribute '__score'
Sleeping......
t.teacher_id: 9527
attention
'''


class Animal:
    pass


class PaxingAni(Animal):
    pass


class Dog(PaxingAni):
    pass


# 实例化 Dog 时，查找到 Dog 的构造函数，参数匹配，不保存
d = Dog()


