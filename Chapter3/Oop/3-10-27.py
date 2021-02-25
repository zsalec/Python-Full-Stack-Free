# 元类演示

# 元类写法是固定的，必须继承自 type
# 元类一般命名以 MetaClass 结尾
class TulingMetaClass(type):
    # 注意以下写法
    def __new__(cls, name, bases, attrs):
        # 自己的业务处理
        print('I am meta class')
        attrs['id'] = '000000'
        attrs['addr'] = '学院路10号'
        return type.__new__(cls, name, bases, attrs)


# 元类定义完就可以使用，使用注意写法
class Teacher(object, metaclass=TulingMetaClass):
    pass


t = Teacher()
print(Teacher.__dict__)
print(t.__dict__)
'''
I am meta class
{'__module__': '__main__', 'id': '000000', 'addr': '学院路10号', '__dict__': <attribute '__dict__' of 'Teacher' objects>, '__weakref__': <attribute '__weakref__' of 'Teacher' objects>, '__doc__': None}
{}
'''
