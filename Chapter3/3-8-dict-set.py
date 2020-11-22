# 关于元组的函数
# - len 获取长度
print('-' * 20)
print('len')
t1 = (1, 2, 3, 4, 5)
print('t1:', t1)
print('len(t1):', len(t1))
'''
--------------------
len
l1: (1, 2, 3, 4, 5)
len(l1): 5
'''

# -- max & min
print('-' * 20)
print('max & min')
print('max(t1): {}, min(t1): {}'.format(max(t1), min(t1)))
'''
--------------------
max & min
max(t1): 5, min(t1): 1
'''

# -- 转化或创建
print('-' * 20)
print('转化或创建')
l2 = [1, 2, 3, 4, 5]
t = tuple(l2)
print(t)
t = tuple()
print(t)
'''
--------------------
转化或创建
(1, 2, 3, 4, 5)
()
'''

# - 元组的函数
# -- count 统计元素的个数
print('-' * 20)
print('count')
t = (2, 3, 1, 1, 3, 34, 56, 1, 2, 3, 3, 2, 2)
print('t:', t)
print('t.count(1):', t.count(1))
'''
--------------------
count
t: (2, 3, 1, 1, 3, 34, 56, 1, 2, 3, 3, 2, 2)
t.count(1): 3
'''

# -- 变量交换
print('-' * 20)
print('变量交换')
a = 1
b = 3
print('before swap: a={},b={}'.format(a, b))
a, b = b, a
print('after swap: a={},b={}'.format(a, b))
'''
--------------------
变量交换
before swap: a=1,b=3
after swap: a=3,b=1
'''


def print_section_header(title):
    print('-' * 20)
    print(title)
    return None


# set 集合
# - 特点：无序，不重复，无索引

# - 定义
print_section_header('定义')
s = set()
print(type(s), s)
s = {}
print(type(s), s)
s = {1}
print(type(s), s)
s = {1, 2}
print(type(s), s)
s = {1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4}
print(s)  # 自动删除重复元素 {1, 2, 3, 4}
'''
--------------------
定义
<class 'set'> set()
<class 'dict'> {}
<class 'set'> {1}
<class 'set'> {1, 2}
{1, 2, 3, 4}
'''

# - 集合的操作
# -- in, not in 成员运算
print_section_header('in, not in')
s = {1, 2, 3, 'a', 'b', 'c'}
print(s)
print('2 in s: {}'.format(2 in s))
print('2 not in s: {}'.format(2 not in s))
'''
--------------------
in, not in
{1, 2, 3, 'b', 'a', 'c'}
2 in s: True
2 not in s: False
'''

# -- 遍历
print_section_header('遍历')
print(type(s), s)
for i in s:
    print(i, end=' ')
s1 = {(1, 2, 3), ('a', 'b', 'c'), (4, 5, 6)}
print(s1)
for i, j, k in s1:
    print('{}, {}, {}'.format(i, j, k))
'''
--------------------
遍历
<class 'set'> {'c', 1, 2, 3, 'b', 'a'}
c 1 2 3 b a {(4, 5, 6), ('a', 'b', 'c'), (1, 2, 3)}
4, 5, 6
a, b, c
1, 2, 3
'''

# -- demo
print_section_header('demo')
s = {23, 2233, 1, 3, 2, 4, 9, 10, 6}
print(s)
s1 = {i for i in s}
print(s1)
s2 = {i for i in s if i % 2 == 0}
print(s2)
'''
--------------------
demo
{1, 2, 3, 4, 6, 9, 10, 23, 2233}
{1, 2, 3, 4, 6, 9, 10, 23, 2233}
{2, 10, 4, 6}
'''
s1 = {1, 2, 3}
s2 = {'a', 'b', 'c'}
print(s1)
print(s2)
s3 = {m * n for m in s2 for n in s1}
print(s3)
'''
{1, 2, 3}
{'b', 'c', 'a'}
{'aaa', 'bb', 'ccc', 'aa', 'b', 'cc', 'c', 'bbb', 'a'}
'''

# - add 向集合添加元素
print_section_header('add')
s = {1, 2, 3, 4, 'a'}
print('before add, id(s): {}, s: {}'.format(id(s), s))
s.add(10)
s.add('b')
print('after add, id(s): {}, s: {}'.format(id(s), s))
'''
--------------------
add
before add, id(s): 39020808, s: {1, 2, 3, 4, 'a'}
after add, id(s): 39020808, s: {1, 2, 3, 4, 10, 'a', 'b'}
'''

# -- remove & discard
# --- remove: 元素不存在时，报错
# --- discard: 元素不存在时，不报错
print_section_header('remove & discard')
s = {1, 2, 3, 33, 4}
print('before remove: id(s): {}, s: {}'.format(id(s), s))
s.remove(3)
print('after remove: id(s): {}, s: {}'.format(id(s), s))
try:
    s.remove(3)
except KeyError:
    print('KeyError: 3')
s.discard(3)
print('after discard: id(s): {}, s: {}'.format(id(s), s))
s.discard(333)  # 不报错
print('after discard 333: id(s): {}, s: {}'.format(id(s), s))
'''
--------------------
remove & discard
before remove: id(s): 36183176, s: {1, 2, 3, 4, 33}
after remove: id(s): 36183176, s: {1, 2, 4, 33}
KeyError: 3
after discard: id(s): 36183176, s: {1, 2, 4, 33}
after discard 333: id(s): 36183176, s: {1, 2, 4, 33}
'''

# - 集合函数
# -- intersection: 交集
# -- difference: 差集
# -- union: 并集
# -- issubset: 是否为子集
# -- issuperset: 是否为超集
print_section_header('集合函数')
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
print('s1:', s1)
print('s2:', s2)
s3 = s1.intersection(s2)
print('intersection(s3):', s3)
s4 = s1.difference(s2)
print('difference(s4):', s4)
print('s1.issubset(s2):', s1.issubset(s2))
print('s3.issubset(s2):', s3.issubset(s2))
print('s1.issuperset(s2):', s1.issuperset(s2))
print('s2.issuperset(s3):', s2.issuperset(s3))
'''
--------------------
集合函数
s1: {1, 2, 3, 4, 5}
s2: {4, 5, 6, 7, 8}
intersection(s3): {4, 5}
difference(s4): {1, 2, 3}
s1.issubset(s2): False
s3.issubset(s2): True
s1.issuperset(s2): False
s2.issuperset(s3): True
'''

# -- frozen set: 冰冻集合
# --- 不可修改
print_section_header('frozen')
s = frozenset()
print('type(s): {}, s:{}'.format(type(s), s))
'''
--------------------
frozen
type(s): <class 'frozenset'>, s:frozenset()
'''

# dict 字典
print_section_header('dict 创建')
d = {}
print('type(d): {}, d: {}'.format(type(d), d))
d = dict()
print('type(d): {}, d: {}'.format(type(d), d))
d = {'one': 1, 'two': 2, 'three': 3}
print('type(d): {}, d: {}'.format(type(d), d))
d = dict({'one': 1, 'two': 2, 'three': 3})
print('type(d): {}, d: {}'.format(type(d), d))
d = dict(one=1, two=2, three=3)
print('type(d): {}, d: {}'.format(type(d), d))
d = dict([('one', 1), ('two', 2), ('three', 3), ('test', 3)])
print('type(d): {}, d: {}'.format(type(d), d))
l1 = ['one', 'tow', 'three']
# - 使用指定的 list 作为键，使用同一值作为键值对的值
d1 = dict.fromkeys(l1, 'haha...')
print('type(d1): {}, d1: {}'.format(type(d1), d1))
'''
--------------------
dict 创建
type(d): <class 'dict'>, d: {}
type(d): <class 'dict'>, d: {}
type(d): <class 'dict'>, d: {'one': 1, 'two': 2, 'three': 3}
type(d): <class 'dict'>, d: {'one': 1, 'two': 2, 'three': 3}
type(d): <class 'dict'>, d: {'one': 1, 'two': 2, 'three': 3}
type(d): <class 'dict'>, d: {'one': 1, 'two': 2, 'three': 3, 'test': 3}
type(d1): <class 'dict'>, d1: {'one': 'haha...', 'tow': 'haha...', 'three': 'haha...'}
'''
dd = {k: v for k, v in d.items()}
print(dd)
dd = {k: v for k, v in d.items() if v % 2 == 0}
print(dd)
'''
{'one': 1, 'two': 2, 'three': 3, 'test': 3}
{'two': 2}
'''

# - 字典特征
# -- 有序，但是无分片和索引
# -- 每个元素都是键值对
# -- key：必须是可哈希的
# -- value：任意值

# -- 访问数据
print_section_header('访问数据')
print('d["one"]:', d['one'])
# --- 键不存在时，抛出 KeyError 异常
try:
    d['four']
except KeyError:
    print("KeyError: 'four'")
# --- 键值不存在，返回 None，或者默认值
print(d.get('100'))
print(d.get('100', 100))
'''
--------------------
访问数据
d["one"]: 1
KeyError: 'four'
None
100
'''

# -- 赋值
print_section_header('赋值')
d['one'] = '一'
print(d)
'''
--------------------
赋值
{'one': '一', 'two': 2, 'three': 3, 'test': 3}
'''

# -- 删除
print_section_header('del')
del d['two']
print(d)
'''
--------------------
del
{'one': '一', 'three': 3, 'test': 3}
'''

# -- in, not in
print_section_header('in, not in')
if 3 in d:
    print('value')
if 'three' in d:
    print('key')
if ('three', 3) in d:
    print('key-value')
'''
--------------------
in, not in
key
'''

# - traverse 遍历
print_section_header('traverse')
for k in d:
    print('{}: {}'.format(k, d[k]))
for k in d.keys():
    print('{}: {}'.format(k, d[k]))
for v in d.values():
    print(v)
'''
--------------------
traverse
one: 一
three: 3
test: 3
one: 一
three: 3
test: 3
一
3
3
'''

print(str(d))  # {'one': '一', 'three': 3, 'test': 3}
i = d.items()
print(type(i), i)  # <class 'dict_items'> dict_items([('one', '一'), ('three', 3), ('test', 3)])
k = d.keys()
print(type(k), k)  # <class 'dict_keys'> dict_keys(['one', 'three', 'test'])
v = d.values()
print(type(v), v)  # <class 'dict_values'> dict_values(['一', 3, 3])
