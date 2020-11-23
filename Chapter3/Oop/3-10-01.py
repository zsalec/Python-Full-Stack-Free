"""
定义一个学生类，用来形容学生
"""


# 定义一个空类
class Student():
    # 一个空类：pass 代表直接跳过
    # 此处 pass 必须有
    pass


# 定义一个对象
mingyue = Student()


# 定义一个类，用来描述听 Python的学生
class PythonStudent():
    # 用 None 给不确定的属性赋值
    name = None
    age = 18
    course = 'Python'

    # 需要注意
    # 1. def doHomework 的缩颈层级
    # 2. 系统默认由一个 self 参数
    def doHomework(self):
        print('I am doing homework...')
        # 推荐在函数末尾使用 return 语句
        return None


# 实例化一个 PythonStudent 的学生，是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
# 注意成员函数的调用没有传递进入参数
yueyue.doHomework()
'''
None
18
I am doing homework...
'''