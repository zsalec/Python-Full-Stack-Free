# str 内建函数
# - 查找类函数
# -- find函数
help(str.find)

# -- index函数
help(str.index)

s = 'I love my native-country, China'
pos = s.find('China')
print(pos)
pos = s.find('America')
print(pos)

try:
    idx = s.index('China')
    print('China is ', idx)
    idx = s.index('America')
    print('America is in ', idx)
except ValueError as e:
    print('error', e)

help(str.rfind)
help(str.lfind)

# - 判断类函数
# -- isalpha
#   - 至少包含一个字符，如果没有，同样返回 False
#   - 汉字认为是 alpha
#   - 注意使用区别，防止被坑（不包含数字，符号，空格，特殊字符
s1 = 'a prime python'
print(s1.isalpha())
s2 = '!@#'
print(s2.isalpha())
s3 = 'abc'
print(s3.isalpha())

'''
- isdigita, isnumeric, isdecimal 判断数字的函数
    Unicode 数字，byte 数字，全角数字（双字节），罗马数字，汉字数字
- islower 小写字符
- startswith/endswith: 判断开头/结尾字符串
- isupper 大写字符
- strip/lstrip/rstrip 删除空字符
- join 拼接
'''

'''
# List 列表
- 一组由有序数据组成的序列
    - 数据有先后顺序
    - 数据可以不是一类数据
- list 的创建
    - 直接创建
    - 使用 list 函数创建
    - 字符串是一个特殊的列表
'''
help(list)
l1 = [1, 2, 3, 4, 5]
print(l1)
l2 = [4, 1, 2, 3, 'Tom', 'Jerry']
print(l2)

# 创建 list
l3 = list()
print(l3)
print(type(l3))

# - list 特例
s = 'I love python'
l1 = list(s)
print(l1)

# 列表常见操作
# - 访问
# -- 索引，从 0 开始，异常 IndexError
l = [23, 43, 234, 5, 66, 12, 44]
print(l[2])
try:
    print(l[111])
except IndexError as e:
    print('IndexError', e)
# - 切片操作，截取一段，生成新的 list
# -- ：, 左包括，右不包括
l1 = l[1:3]
print(l1)
print('l[0]: {}, l1[0]: {}'.format(l[0], l1[0]))
print(id(l))
print(id(l1))
print(l[1:])  # 从 1 开始
print(l[::2])  # 步长为 2
print(l[3:100])  # 下标可以溢出
print(l[::-2])  # 可以为负数，负数表示从右开始
print(l[-2:-5])  # 为空，应为起始位置应该小于截止位置
print(l[-5:-2])
