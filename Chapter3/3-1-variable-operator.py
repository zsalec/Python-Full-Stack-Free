# 字符串
# - 转义字符
# - 格式化
# - 内建函数

# - 转义字符
s = 'I Love Python'
print(s)  # I Love Python

# -- 表示 ' 的方法
# --- 引号嵌套
# --- 转义字符 \'
s1 = "Let's go"
print(s1)  # Let's go
s2 = 'Let\'s go'
print(s2)  # Let's go

# \\ ==> \
s3 = 'c:\\user'
print(s3)  # c:\user

# 回车换行
s5 = 'I love\r\nPython'
print(s5)
'''
I love
Python
'''

# - 格式化
# -- 利用 %
s = 'I love %s'
print(s)  # I love %s
print(s % 'Python')  # I love Python
s = 'I am %d years old.'
print(s)  # I am %d years old.
print(s % 18)  # I am 18 years old.
s = 'I am %s, I am %d years old'
# -- 参数的数量等于占位符数，并且类型一致
print(s % ('Alec', 18))  # I am Alec, I am 18 years old

# -- 利用 format
help(str.format)
s = 'Yes, I am {1} years old. I am {0}, I am {1} years old.'
print(s.format('Alec', 46))  # Yes, I am 46 years old. I am Alec, I am 46 years old.

# - None
# -- 表示什么也没有
# -- 如果函数没有返回值，可以返回 None
# -- 用来占位
# -- 用来接触变量的绑定

# 表达式
# - 由一个或多个数字或变量和运算符组合成的一段代码
# - 通常会返回一个结果

# 运算符
# - 运算：由一个或多个值经过变化得到新值得过程
# - 运算符：用于运算的符号
# - 分类
# -- 算术运算
# -- 比较/关系运算
# -- 逻辑运算
# -- 赋值运算
# -- 位运算
# -- 成员运算
# -- 身份运算

# -- 算术运算符
# --- + - * / % // **
a = 9 + 3 - 2
print(a)  # 10
a = 5 * 2
print(a)  # 10
a = 9 / 4
print(a)  # 2.25
a = 9 // 4
print(a)  # 2
a = 9 % 4
print(a)  # 1
print(3 ** 4)  # 81
# 整除是向下取整 (floor divide)
print(9 // -4)  # -3
print(-9 // 4)  # -3
# 取模：向下取整后的余数
print(9 % -4)  # -3
print(-9 % 4)  # 3

# -- 比较运算符
# --- == != > >= < <=
# --- 结果是布尔值
a = 3 ** 4  # 81
b = a == 80
print(b)  # False
print(9 != 8)  # True

# -- 赋值运算符
# --- = += -= /= *= %= //= **=
a = 0
c = a = 4
a += 7
print(a)  # 11

# -- 逻辑运算符
# --- and or not
# --- 没有异或运算符
# --- 先 and 后 or
a = True
b = False
c = True
d = a and b or c
print(d)  # True
e = a or c and b
print(e)  # True

# --- 逻辑运算的短路

# -- 成员运算
# --- in,  not in
lst = [1, 2, 3, 4, 5]
a = 7
b = a in lst
print(b)  # False
a = 4
print(a in lst)  # True
print(a not in lst)  # False

# -- 身份运算
# --- is
a = 9
b = 9
print('a is b =', a is b)  # a is b = True
c = 3
d = 6
e = c + d
print('a is e =', a is e)  # a is e = True
s1 = 'I love Python'
s2 = 'I love Python'
print('s1 is s2 = ', s1 is s2)  # s1 is s2 =  True
s3 = 'I love '
s4 = 'Python'
s5 = s3 + s4
print(s1)
print(s5)
print('s1 == s5:', s1 == s5, 's1 is s5 =', s1 is s5)  # s1 == s5: True s1 is s5 = False

# - 运算符的优先级
# -- 括号的优先级最高
# -- ** 幂
# -- ~ + - 位运算
# -- * / % //
# -- + -
# -- >> << 位移
# -- & 位与
# -- ^ | 位异或，或
# -- <= < > >= 比较运算
# -- <> == != 等于运算符
# -- = += -= *= /= //= %= **=
# -- is, not is 身份运算
# -- not or and 逻辑运算
