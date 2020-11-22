# 变量赋值

# 查看关键字的方法
import keyword  # 引入关键字模块

# 打印出系统全部关键字
print(keyword.kwlist)
# output: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def',
# 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
# 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
print(keyword.iskeyword('False1'))  # False
print(keyword.iskeyword('False'))   # True

# 定义变量
age = 18
print(age)  # 18
print(18)   # 18

age1 = age2 = age3 = 18
print(age1)     # 18
print(age2)     # 18
print(age3)     # 18

age4, age5, age6 = 18, 19, 20
print(age4)     # 18
print(age5)     # 19
print(age6)     # 20
