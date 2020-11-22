# 递归
# - Hanno Town
# -- 一次只能移动一个盘子
# -- 小盘子必须在上方
from typing import List

a1 = 'A'
b1 = 'B'
c1 = 'C'


def hanno(a, b, c, level):
    if level > 0:
        hanno(a, c, b, level - 1)
        print('{} ==> {}'.format(a, c))
        hanno(b, a, c, level - 1)
    return None


for i in range(1, 4):
    print('Town of Hanno (level: {})'.format(i))
    hanno(a1, b1, c1, i)
'''
Town of Hanno (level: 1)
A ==> C
Town of Hanno (level: 2)
A ==> B
A ==> C
B ==> C
Town of Hanno (level: 3)
A ==> C
A ==> B
C ==> B
A ==> C
B ==> A
B ==> C
A ==> C
'''

# - del 删除。不生成新列表
l2 = [1, 2, 3, 4, 5]
print('before delete, id(l2): {}'.format(id(l2)))
print(l2)
del l2[2]
print('after delete, id(l2): {}'.format(id(l2)))
print(l2)
'''
before delete, id(l2): 30298696
[1, 2, 3, 4, 5]
after delete, id(l2): 30298696
[1, 2, 4, 5]
'''

# - + 列表相加
# -- 将列表元素合并，组成一个新的列表
a = [1, 2, 3]
b = [4, 5, 6]
c = ['a', 'b', 'c']
d = a + b + c
print(d)  # [1, 2, 3, 4, 5, 6, 'a', 'b', 'c']

# - * 列表乘运算
# -- 相当于将多个列表组成新列表
a = [1, 2, 3]
b = a * 3
print(b)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# - in, not in 成员运算
b = 2
print('b in a: {}'.format(b in a))  # b in a: True
print('b not in a: {}'.format(b not in a))  # b not in a: False
c = 8
print('c in a: {}'.format(c in a))  # c in a: False
print('c not in a: {}'.format(c not in a))  # c not in a: True

# - 遍历
for i in a:
    print(i)
'''
1
2
3
'''

s = 'I love Python!'
for i in s:
    print(i)
'''
I
 
l
o
v
e
 
P
y
t
h
o
n
!
'''

print(type(range(1, 10)))  # <class 'range'>

length = len(a)
index = 0
while index < length:
    print(a[index])
    index += 1
'''
1
2
3
'''

# -- 双层列表(嵌套列表)
a = [['one', 1], ['two', 2], ['three', 3]]
for k, v in a:
    print('{} ==> {}'.format(k, v))
'''
one ==> 1
two ==> 2
three ==> 3
'''

# -- 嵌套列表的变形
a = [['one', 1, 'Tonny'], ['two', 2], ['three', 3, 4, 5]]
try:
    for k, v in a:
        print('{} ==> {}'.format(k, v))
except ValueError:
    print('error: too many values to unpack')
'''
error: too many values to unpack
'''

a = [['one', 1, 'Tom'], ['two', 2, 'Jerry'], ['three', 3, 'Mickey']]
for k, v, n in a:
    print('{} ==> {}.{}'.format(k, v, n))
'''
one ==> 1.Tom
two ==> 2.Jerry
three ==> 3.Mickey
'''

# - 用 for 创建新列表
a = ['a', 'b', 'c']
b = [i for i in a]  # ['a', 'b', 'c']
print(b)
# -- 加入算术运算
c = [i * 10 for i in a]  # ['aaaaaaaaaa', 'bbbbbbbbbb', 'cccccccccc']
print(c)

# -- 过滤元素
a = [i for i in range(1, 30)]
b = [i for i in a if i % 2 == 0]
print(b)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

# -- 嵌套
a = [i for i in range(1, 4)]
print(a)  # [1, 2, 3]
b = [i * 100 for i in range(1, 4)]
print(b)  # [100, 200, 300]
c = [m + n for m in a for n in b]
print(c)  # [101, 201, 301, 102, 202, 302, 103, 203, 303]

# 列表的函数
# - len 列表长度
a = [x for x in range(1, 100)]
print('len(a) = {}'.format(len(a)))  # len(a) = 99
# - max 最大值
print('max(a) = {}'.format(max(a)))  # max(a) = 99
# - min 最小值
print('min(a) = {}'.format(min(a)))  # min(a) = 1
