# OOP
# - 思想
# -- 以模块化解决工程问题
# -- 面向对象 vs 面向过程

# - 常见名称
# -- OO: Orient Object 面向对象
# -- 00a: 分析
# -- ood: 设计
# -- 00p: 编程
# -- 00i: 实现
# -- ooa --> ood --> ooi    # oom -> #oo

# - 类 vs 对象
# -- 类：抽象，描述的是一个集合，侧重于共性
# -- 对象：具象，描述的是个体

# - 类的内容
# -- 动作：函数
# -- 属性：变量

# - is-a

'''
# 定义类： class 关键字
# 类命名
- 大驼峰命名法
'''

# - 类定义
class Student:
    # 此处定义一个空类
    # pass 是关键字，表示占位用的，无意义
    pass


# - 定义对象
tommy = Student()


class PythonStudent:
    name = "none"
    age = 18
    course = 'Python'

    '''
    定义类中的函数
    一般需要有 self 关键字
    其余跟普通函数基本相同
    '''
    def give_money(self):
        pass


william = PythonStudent()
print(william.name)
print(william.age)
print(william.course)
