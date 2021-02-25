# 利用 type 造一个类

# 先定义类应具有的成员函数
def say(self):
    print('Say......')
    return None


def talk(self):
    print('Talking......')
    return None


# 用 type 来创建一个类
A = type('B', (object,), {'class_say': say, 'class_talk': talk})
a = A()
a.class_say()
a.class_talk()
print(A.__dict__)
print(a.__dict__)
'''
Say......
Talking......
{'class_say': <function say at 0x0000000001E54318>, 'class_talk': <function talk at 0x0000000001E54558>, '__module__': '__main__', '__dict__': <attribute '__dict__' of 'B' objects>, '__weakref__': <attribute '__weakref__' of 'B' objects>, '__doc__': None}
{}
'''
