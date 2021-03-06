"""
# 表达式
- 由一个或多个数字或变量或运算符组成的代码
- 通常返回一个结果
1 + 2
"""

# 表达式案例
a = 1 + 2

"""
# 运算符
- 有一个以上的值经过一系列的运算得到新值得过程就叫运算
- 用来操作运算的符号叫运算符
- 运算符分类
    - 算术运算符
    - 比较或者关系运算符
    - 赋值运算符
    - 逻辑运算符
    - 位运算符
    - 成员运算符
    - 身份运算符
"""

'''
# 算术运算符
- 用来进行算数运算的符号
- 通常用来表示加减乘除
- Python 没有自增、自减运算符
'''
# 算数运算符案例
# 加减乘除跟数学意义基本一致
a = 9 - 2
print('9 - 2 = ', a)  # 9 - 2 = 7

b = 9 + 2
print('9 + 2 = ', b)  # 9 + 2 = 11

c = 8 * 2
print('8 * 2 = ', c)  # 8 * 2 = 16

# Python 除法分为普通除法，整除，取模

# 正常除法
# 此操作符在 Python 2.x 和 3.x 有些不同
d = 9 / 2   # 除
print('9 / 2 = ', d)  # 9 / 2 = 4.5
# 除以负数的结果
a = 9 / -4
print(f'9 / -4 = {a}')  # 9 / -4 = -2.25

# 地板除，取整
e = 9 // 2  # 整除
print('9 // 2 = ', e)  # 9 // 2 = 4
# 取余
f = 9 % 2   # 取模
print('9 % 2 = ', f)  # 9 % 2 = 1
# 取模结果的符号要和除数一致
g = 9 % -4  # 取模 -3
print('9 % -4 = ', g)  # 9 % -4 = -3
