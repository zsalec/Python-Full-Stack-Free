# demo
# - 传址
def an(n):
    n[2] = 300
    print(n)
    return None


# - 传值
def bn(n):
    n += 100
    print(n)
    return None


a = [1, 2, 3, 4, 5]
b = 9

print('a:', a)
an(a)
print('a:', a)
'''
a: [1, 2, 3, 4, 5]
[1, 2, 300, 4, 5]
a: [1, 2, 300, 4, 5]
'''

print('b:', b)
bn(b)
print('b:', b)
'''
b: 9
109
b: 9
'''

# 关于列表的函数
# - append 追加
print('-' * 20)
print('append')
a = [i for i in range(1, 10)]
print(a)
a.append(100)
print(a)
'''
--------------------
append
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
'''

# - 插入
print('-' * 20)
print('insert')
print(a)
a.insert(2, 200)
print(a)
'''
--------------------
insert
[1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
[1, 2, 200, 3, 4, 5, 6, 7, 8, 9, 100]
'''

# - remove 删除
print('-' * 20)
print('remove')
print(a)
a.remove(7)
print(a)
'''
--------------------
remove
[1, 2, 200, 3, 4, 5, 6, 7, 8, 9, 100]
[1, 2, 200, 3, 4, 5, 6, 8, 9, 100]
'''

# - pop 弹出最后一个元素
# -- 在原列表中弹出
# -- index 超出范围报错
print('-' * 20)
print('pop')
last_elem = a.pop()
print(last_elem)
print(a, id(a))
elem = a.pop(-4)
print(elem, a, id(a))
first_elem = a.pop(0)
print(first_elem, a)
try:
    elem = a.pop(100)
    print(elem, a)
except IndexError:
    print('IndexError: pop index out of range')
'''
--------------------
pop
100
[1, 2, 200, 3, 4, 5, 6, 8, 9] 30233672
5 [1, 2, 200, 3, 4, 6, 8, 9] 30233672
1 [2, 200, 3, 4, 6, 8, 9]
IndexError: pop index out of range
'''

# -- remove 删除指定值元素
# --- 在元列表中删除
# --- 值不存在时，报错
print('-' * 20)
print('remove')
b = 6
print(id(a))
a.remove(b)
print(id(a), a)
try:
    a.remove(b)
except ValueError:
    print('ValueError: list.remove(x): x not in list')
'''
remove
30495816
30495816 [2, 200, 3, 4, 8, 9]
ValueError: list.remove(x): x not in list
'''

# -- clear 清空列表
# --- 清空元列表
print('-' * 20)
print('clear')
print(id(a), a)
a.clear()
print(id(a), a)
'''
--------------------
clear
30430280 [2, 200, 3, 4, 8, 9]
30430280 []
'''

# -- reverse 反转
# --- 在原列表中进行
print('-' * 20)
print('reverse')
a = [1, 2, 3, 4, 5, 6, 8, 7]
print('before reverse:', id(a), a)
a.reverse()
print('after reverse:', id(a), a)
'''
--------------------
reverse
before reverse: 3822152 [1, 2, 3, 4, 5, 6, 8, 7]
after reverse: 3822152 [7, 8, 6, 5, 4, 3, 2, 1]
'''

# -- extend 列表扩展
print('-' * 20)
print('extend')
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9]
print('before extend,', id(a), a, b)
a.extend(b)
print('after extend,', id(a), a, b)
'''
--------------------
extend
before extend, 1791048 [1, 2, 3, 4, 5] [6, 7, 8, 9]
after extend, 1791048 [1, 2, 3, 4, 5, 6, 7, 8, 9] [6, 7, 8, 9]
'''

# -- count 计数
# --- 针对某一特定值
print('-' * 20)
print('count')
print(a)
a.append(10)
a.insert(0, 10)
print(a)
a_len = a.count(10)
print(a_len)
'''
--------------------
count
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
2
'''

# -- copy 浅拷贝
print('-' * 20)
print('copy')
print('a = b: 传址')
b = a
print('id(a): {}, id(b): {}, id(a)==id(b): {}'.format(id(a), id(b), id(a) == id(b)))
print('before let, a:', a)
print('before let, b:', b)
b[3] = 777
print('after let, a:', a)
print('after let, b:', b)
'''
--------------------
copy
a = b: 传址
id(a): 1725512, id(b): 1725512, id(a)==id(b): True
before let, a: [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
before let, b: [10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
after let, a: [10, 1, 2, 777, 4, 5, 6, 7, 8, 9, 10]
after let, b: [10, 1, 2, 777, 4, 5, 6, 7, 8, 9, 10]
'''
print('*' * 20)
print('b = a.copy(): 传值')
b = a.copy()
print('id(a): {}, id(b): {}, id(a)==id(b): {}'.format(id(a), id(b), id(a) == id(b)))
print('before let, a:', a)
print('before let, b:', b)
b[3] = 111
print('after let, a:', a)
print('after let, b:', b)
'''
********************
b = a.copy(): 传值
id(a): 1725512, id(b): 1725000, id(a)==id(b): False
before let, a: [10, 1, 2, 777, 4, 5, 6, 7, 8, 9, 10]
before let, b: [10, 1, 2, 777, 4, 5, 6, 7, 8, 9, 10]
after let, a: [10, 1, 2, 777, 4, 5, 6, 7, 8, 9, 10]
after let, b: [10, 1, 2, 111, 4, 5, 6, 7, 8, 9, 10]
'''

# -- 深拷贝和浅拷贝的区别
print('-' * 20)
a = [1, 2, 3, [10, 20, 30]]
b = a.copy()
print('id(a[3]): {}, id(b[3]): {}, id(a[3])==id(b[3]): {}'.format(id(a[3]), id(b[3]), id(a[3]) == id(b[3])))
'''
--------------------
id(a[3]): 36393160, id(b[3]): 36393160, id(a[3])==id(b[3]): True
'''

# tuple - 元组
# - 可以看做不可更改的数值

# - 创建
print('-' * 20)
print('tuple')
t = ()
print(type(t), t)
t = (1,)
print(type(t), t)
t = 1,
print(type(t), t)
t = (1, 2, 3, 4)
print(type(t))
t = 1, 2, 3, 4, 5
print(type(t), t)
l1 = [1, 2, 3, 4, 5]
t = tuple(l1)
print(type(t), t)
'''
--------------------
tuple
<class 'tuple'> ()
<class 'tuple'> (1,)
<class 'tuple'> (1,)
<class 'tuple'>
<class 'tuple'> (1, 2, 3, 4, 5)
<class 'tuple'> (1, 2, 3, 4, 5)
'''

# - 元组的特性
# -- 不能修改
# -- 元组数据可以是任意类型
# -- 有序

# - 索引操作
print('-' * 20)
print('index')
print('t[0]: {}'.format(t[0]))
try:
    print(t[100])
except IndexError:
    print('IndentationError: unexpected indent')
'''
--------------------
index
t[0]: 1
IndentationError: unexpected indent
'''

# - 切片
# -- 可以超标
print('-' * 20)
print('切片')
t = (1, 2, 3, 4, 5, 6)
t1 = t[1::2]
print('t:', t)
print('t1:', t1)
print('id(t): {}, id(t1): {}, id(t)==id(t1): {}'.format(id(t), id(t1), id(t) == id(t1)))
print('t[1:100]', t[1:100])
'''
--------------------
切片
t: (1, 2, 3, 4, 5, 6)
t1: (2, 4, 6)
id(t): 31317160, id(t1): 38723240, id(t)==id(t1): False
t[1:100] (2, 3, 4, 5, 6)
'''

# -- + 运算
print('-' * 20)
print('+ operator')
t1 = (1, 2, 3)
t2 = (3, 4, 5)
print('id(t1):', id(t1), t1)
t1 += t2
print('id(t1):', id(t1), t1)
'''
--------------------
+ operator
id(t1): 38722920 (1, 2, 3)
id(t1): 39203080 (1, 2, 3, 3, 4, 5)
'''

# -- * 运算
print('-' * 20)
print('* operator')
t1 = (1, 2, 3)
t2 = t1 * 3
print('t1', t1)
print('t1 * 3:', t2)
'''
--------------------
* operator
t1 (1, 2, 3)
t1 * 3: (1, 2, 3, 1, 2, 3, 1, 2, 3)
'''

# -- in, not in 成员运算
print('-' * 20)
print('in, not in operator')
print('2 in t1:', 2 in t1)
print('2 not in t1:', 2 not in t1)
'''
--------------------
in, not in operator
2 in t1: True
2 not in t1: False
'''

# -- 遍历
print('-' * 20)
print('遍历')
for i in t1:
    print(i)
'''
--------------------
遍历
1
2
3
'''
# -- 双层元组遍历
t = ((1, 2, 3), ('a', 'b', 'c'), (1.1, 2.2, 3.3))
for i in t:
    print(i)
for i, j, k in t:
    print('{}, {}, {}'.format(i, j, k))
'''
(1, 2, 3)
('a', 'b', 'c')
(1.1, 2.2, 3.3)
1, 2, 3
a, b, c
1.1, 2.2, 3.3
'''
