# 构造函数 Demo
class Person:
    # 实例化时，需要确定 姓名，年龄，地址
    def __init__(self):
        self.name = 'NoName'
        self.age = 18
        self.address = "Student's dormitory"
        print('In init func')
        return None


# 实例化 Person
p = Person()
print(p.__dict__)
'''
In init func
{'name': 'NoName', 'age': 18, 'address': "Student's dormitory"}
'''
