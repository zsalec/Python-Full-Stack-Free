'''
# 逻辑运算
#
# @ Author: Your name
# @ Create Time: 2021-02-06 09:36:16
# @ Modified by: Your name
# @ Modified time: 2021-02-07 00:07:44
# @ Description:
'''

# 运算符
# 指数
# 两个乘号就是指数
a = 7 ** 2
print('7 ** 2 = ', a)  # 7 ** 2 = 49

"""
# 比较运算符
- 对两个内容进行比较的运算符
- 结果一定是布尔值，即 True/False
"""
# 等于 ==
a = 3 == 4
print('3 == 4 is', a)  # 3 == 4 is False

# 不等于 !=
a = 3 != 4
print(f'3 != 4 is {a}')  # 3 != 4 is True

# 其他比较运算符
# >, >=, <, <=
b = 3 >= 8
print('3 >= 8 is', b)  # 3 >= 8 is False
b = 'Python' > 'C'
print(f'Python > C is {b}')  # Python > C is True

"""
# 赋值运算符
- 把一个值放到变量里边去
"""
# 赋值运算符 =
a = 9

# 复杂赋值
a = b = 9
a, b = 1, 2

# 赋值的缩写
# +=, -=, *=, /=, //=, **=, %=
cc = 100
cc = cc + 3  # cc 使用前必须赋值（初始化）
print('after cc = cc + 3, cc is', cc)  # after cc = cc + 3, cc is 103
cc += 3
print('after cc += 3, cc is ', cc)  # after cc += 3, cc is  106

"""
# 逻辑运算符
- 对布尔类型变量或者值进行运算的符号
- and：逻辑与
- or：逻辑或
- not：逻辑非
- Python 里面的逻辑运算符没有异或
- 运算规则
    - and 看做惩罚，or 看做加法
    - True 看做 1，False 看做 0
    - 则逻辑运算就能转换成整数数学运算
    - 最后结果如果为 0 则为 False，否则为 True
- 逻辑运算的短路问题
    - 逻辑运算是，按照运算顺序计算，一旦能够确定整个式子未来的值，则不再进行计算，直接返回
"""

# 逻辑表达式举例
a = True
b = True
c = False

aa = a and b  # 左边表达式可以转换成 1 * 1
print(f'{a} and {b} is {aa}')  # True and True is True

bb = a and c
print(f'{a} and {c} is {bb}')  # True and False is False

cc = 100 and c
print(f'100 and {c} is {cc}')  # 100 and False is False

# 布尔值跟数字的转换
# 数字转布尔值的时候：0 = False，非零 = True
# 布尔值转数字的时候：True = 1, False = 0

# 短路问题案例
a = True
b = True
c = False

aa = a or b and (a and b)  # 转换成运算 1 + ....
print(aa)  # True

# 短路问题案例 2


def func_a():
    print('a')
    return True


def func_b():
    print('b')
    return True


if func_a() and func_b():
    print('AAAAAA')
'''
a
b
AAAAAA
'''

# 字符串乘以数字，表示对这个字符串重复多少遍
print('*' * 20)
if func_a() or func_b():
    print('BBBBBBB')
'''
********************
a
BBBBBBB
'''

"""
# 成员运算符
- 用来检测一个值或者变量是否在某个集合里面
- in：成员运算符
- not in：不在里边的意思
"""

# in 案例
L = [1, 2, 3, 4, 5]
a = 6
aa = a in L
print(f'{a} in {L} is {aa}')  # 6 in [1, 2, 3, 4, 5] is False
# a 没有在 L 里面
aa = a not in L
print(f'{a} not in {L} is {aa}')  # 6 not in [1, 2, 3, 4, 5] is True

"""
# 身份运算符
- 用来确定两个变量是否是同一个变量
- is：是身份运算符
- not is：不是身份运算符
"""

# 身份运算符定义
a = 1
b = 100
aa = a is b
print(f'a({a}) is b({b}) = {aa}') # a(1) is b(100) = False
a = 10000000000989888
b = 10000000000989888
aa = a is b
print(f'a({a}) is b({b}) = {aa}')
# 在 Python 3.9 中
# a(10000000000989888) is b(10000000000989888) = True
# 在 Python 3.7 中
# a(10000000000989888) is b(10000000000989888) = False
a = 5
b = 5
aa = a is b
print(f'a({a}) is b({b}) = {aa}')

"""
# 运算符优先级问题
- 小括号具有最高优先级
>** 指数（坐高优先级）
>~ + - 按位翻转，一元加号和减号（最后两个的方法名为 +@ 和 -@
>* / % // 乘，除，取模，取整除
+ - 加法，减法
>> << 右移，左移
& 按位与
^ | 异或，或位运算
<= < > >= 比较运算符
<> == != 关系运算符
= %= /= //= += -= *= **= 赋值运算符
is is not 身份运算符
in not in 成员运算符
not or and 逻辑运算符
"""