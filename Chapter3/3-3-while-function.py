# while 循环
# - for 循环 - 确定循环次数
# - while 循环 - 不确定循环次数，只知道退出条件
# -- while 条件表达式:
# --    语句块

# 利率 6.7%，计算翻倍的年限
rate = 0.067
year = 0
capital = 10000
while capital < 20000:
    capital *= 1 + 0.067
    year += 1
    print('No. {:} years, capital: {:.1f}'.format(year, capital))
print('After {} years, capital will be doubled'.format(year))
'''
No. 1 years, capital: 10670.0
No. 2 years, capital: 11384.89
No. 3 years, capital: 12147.677629999998
No. 4 years, capital: 12961.572031209998
No. 5 years, capital: 13829.997357301068
No. 6 years, capital: 14756.607180240238
No. 7 years, capital: 15745.299861316334
No. 8 years, capital: 16800.23495202453
No. 9 years, capital: 17925.85069381017
No. 10 years, capital: 19126.88269029545
No. 11 years, capital: 20408.383830545245
After 11 years, capital will be doubled
'''


# 函数
# - 代码的一种组织形式
# - 一个函数一般完成一项特定的功能
# - 函数使用
# -- 函数需要先定义
# -- 使用函数，俗称调用
def func():
    print('This is a function')
    print('It can finish a special function')


func()  # This is a function


# 函数参数和返回值
# - 形参，实参
# -- person 形参
# - return 结束函数
def hello(person):
    print('{}, what\'s wrong'.format(person))
    print('Sir, 你不理我，我就走了！')
    s = '我已经跟{0}打过招呼了，{0}不理我'.format(person)
    # -- s 返回值
    return s
    print('不会被执行！！！')


t = 'Moon'
# -- t 实参
result = hello(t)
'''
Moon, what's wrong
Sir, 你不理我，我就走了！
'''
print(result)  # 我已经跟Moon打过招呼了，Moon不理我


# demo
def print_table():
    def print_line(no):
        for i in range(1, no + 1):
            print('{} x {} = {}'.format(i, no, i * no), end='\t')
        print()
        return None

    for i in range(1, 10):
        print_line(i)


print_table()
'''
1 x 1 = 1	
1 x 2 = 2	2 x 2 = 4	
1 x 3 = 3	2 x 3 = 6	3 x 3 = 9	
1 x 4 = 4	2 x 4 = 8	3 x 4 = 12	4 x 4 = 16	
1 x 5 = 5	2 x 5 = 10	3 x 5 = 15	4 x 5 = 20	5 x 5 = 25	
1 x 6 = 6	2 x 6 = 12	3 x 6 = 18	4 x 6 = 24	5 x 6 = 30	6 x 6 = 36	
1 x 7 = 7	2 x 7 = 14	3 x 7 = 21	4 x 7 = 28	5 x 7 = 35	6 x 7 = 42	7 x 7 = 49	
1 x 8 = 8	2 x 8 = 16	3 x 8 = 24	4 x 8 = 32	5 x 8 = 40	6 x 8 = 48	7 x 8 = 56	8 x 8 = 64	
1 x 9 = 9	2 x 9 = 18	3 x 9 = 27	4 x 9 = 36	5 x 9 = 45	6 x 9 = 54	7 x 9 = 63	8 x 9 = 72	9 x 9 = 81	
'''


def stu(**kwargs):
    print('Arguments:')
    print(type(kwargs))
    for k, v in kwargs.items():
        print('{} = {}'.format(k, v))
    return None


stu(name='Tom', age=18, learn='Python')
'''
Arguments:
<class 'dict'>
name = Tom
age = 18
learn = Python
'''


# - 收集参数混合调用的顺序问题
# -- 顺序：普通参数 > 关键字参数 > 收集参数
def student(name, age, *args, hobby='None', **kwargs):
    print('Hello，大家好')
    print('My name is {}, is {} years old'.format(name, age))
    if hobby is None:
        print('I have none hobby')
    else:
        print('My hobby is', hobby)
    print('*' * 30)
    for i in args:
        print(i)
    print('*' * 30)
    for k, v in kwargs.items():
        print(k, '--', v)
    return None


name = 'Tonny'
age = 19
student(name, age)
'''
Hello，大家好
My name is Tonny, is 19 years old
My hobby is  None
******************************
******************************
'''
student(name, age, hobby='basketball')
'''
Hello，大家好
My name is Tonny, is 19 years old
My hobby is  basketball
******************************
******************************
'''
student(name, age, 'swimming', v2='param1', v3='param2', v1='param3')
'''
Hello，大家好
My name is Tonny, is 19 years old
My hobby is  basketball
******************************
******************************
Hello，大家好
My name is Tonny, is 19 years old
My hobby is None
******************************
swimming
******************************
v2 -- param1
v3 -- param2
v1 -- param3
'''
student(name, age, 'Python', 'C++', hobby='hiking', a1='p1', a2='p2', a3='p3')
'''
Hello，大家好
My name is Tonny, is 19 years old
My hobby is hiking
******************************
Python
C++
******************************
a1 -- p1
a2 -- p2
a3 -- p3
'''


# -- 收集参数的解包问题
# --- 把参数放到 list/dict 中

# demo
def stu1(*args):
    print('=' * 30)
    n = 0
    for i in args:
        n += 1
        print(n, type(i), i)
    return None


l1 = {'Tonny', 10, 2, 'Hello'}
# l1 作为一个变量收集到 args 中
stu1(l1)
'''
==============================
1 <class 'set'> {'Hello', 10, 2, 'Tonny'}
'''

# - l1 解包后 收集到 args 中
stu1(*l1)
'''
==============================
1 <class 'str'> Hello
2 <class 'int'> 10
3 <class 'int'> 2
4 <class 'str'> Tonny
'''


# 返回值
def func1():
    print('有返回值')
    return 1


def func2():
    print('没有返回值')


f1 = func1()
print(f1)
'''
有返回值
1
'''
# - 默认返回 None
f2 = func2()
print(f2)
'''
没有返回值
None
'''


# 函数文档
# -- 写法
# -- 1. 第一行用三引号定义符
# -- 2. 一般具有固定格式
# --
# - 文档查看
def func3(name, age, *args):
    '''
    这是文档演示
    :param name: 姓名
    :param age: 年龄
    :param args: 其他参数
    :return: None
    '''
    print('This is function func3')


help(func3)
'''
Help on function func3 in module __main__:

func3(name, age, *args)
    这是文档演示
    :param name: 姓名
    :param age: 年龄
    :param args: 其他参数
    :return: None
'''

print(func3.__doc__)
'''
    这是文档演示
    :param name: 姓名
    :param age: 年龄
    :param args: 其他参数
    :return: None
'''
