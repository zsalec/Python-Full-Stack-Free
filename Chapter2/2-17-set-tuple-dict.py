# tuple 元组
# - 可以理解为一个不可修改的列表
def printElement(var):
    print(type(var), var)
    return None


ta = ()  # 空元组
printElement(ta)
ta = (100,)  # 只有一个元素的时，需要添加逗号表明是元组，而不是数字
printElement(ta)
ta = 100,
printElement(ta)
ta = 100, 200
printElement(ta)
ta = 1, 2, 3, 'I Love Python'
printElement(ta)

# - 有序
la = ['I', 'love', 'Python', 'A']
printElement(la)
ta = tuple(la)
printElement(ta)

# - 切片
print(ta[:])
print(ta[:2])
print(ta[-1::-1])  # 反转

# - 元组相加
ta = 100, 200, 300
tb = 'I', 'love', 'Python'
tc = ta + tb
print(tc)

# - 元组乘
tc = tb * 2
print(tc)  # ('I', 'love', 'Python', 'I', 'love', 'Python')

# - 成员检测
if 'Python' in tc:
    print('love Python')
else:
    print('Don\'t love Python')

# - 元组遍历
for i in tc:
    print(i, end=' ')
print()

# - 元组嵌套
ta = (10, 20, 30), ('I', 'love', 'Python'), ('Hello', 'world', '!')
for r in ta:
    print(r)

for r in ta:
    for c in r:
        print(c, end=' ')
    print()

# - 子元组的元素个数必须一致
for i, j, k in ta:
    print(i, j)

# - 长度
print(len(ta))

ta = [1, 1, 23, 33, 212, 23, 54, 52, 1]
# - 最大值
print(max(ta))

# - 最小值
print(min(ta))

# - count 计数
print(ta.count(1))

# - index 索引
print(ta.index(23))

# 交换数值
a = 10
b = 20
print('Before swapping, a: {}, b: {}'.format(a, b))
a, b = b, a
print('After swapping, a: {}, b: {}'.format(a, b))

# 集合
# - 和数学集合的概念一致
# - 内容无序，内容不重复
sa = set()
print(sa)
li = [1, 2, 1, 3, 1, 5, 1, 7, 1, 9]
sb = set(li)
print(sb)

sc = {123, 1, 2, 1, 3, 1, 5, 1, 7, 1, 9}
print(sc)

# -- in
if 2 in sc:
    print('2 in sc')

if 12 in sc:
    print('12 in sc')
else:
    print('12 is not in sc')

# -- 遍历集合
for i in sc:
    print(i, end=' ')
print()

sd = {(1, 2, 3), ('a', 'b', 'c'), ('Tom', 'Jerry', 'Mickey')}
for i, j, k in sd:
    print(i, j, k)
print(sd)

# - 集合生成式
sa = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
sb = {i for i in sa}
print(sb)
sc = {i for i in sa if i % 2 == 0}
print(sc)  # {2, 4, 6, 8, 10}

# -- 每个元素平方，建立新的集合
sd = {i ** 2 for i in sa}
print(sd)  # {64, 1, 4, 36, 100, 9, 16, 49, 81, 25}
se = {m * n for m in sa for n in sa}
print(se)
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 24, 25, 27, 28, 30, 32, 35, 36, 40, 42, 45, 48, 49, 50,
# 54, 56, 60, 63, 64, 70, 72, 80, 81, 90, 100}

# - 集合的函数
# -- len 长度
print(len(sd), len(se))  # 10 42
# -- max/min 极值
print(max(sa), min(sa))  # 10 1
# -- add 添加元素
print(sa)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
sa.add(100)
print(sa)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100}
# -- 清空
se.clear()
print(se)  # set()
# -- remove 删除
sa.remove(100)
print(sa)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
try:
    sa.remove(100)  # 抛出异常
    print(sa)  # 不执行
except KeyError:
    print('在集合sa中，100不存在')
# -- discard 删除。删除不存在值时，不会抛出异常
sa.add(100)
print(sa)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100}
sa.discard(100)
print(sa)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
sa.discard(100)
print(sa)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# -- pop 弹出。由于集合无序，所以弹出值不确定，因此，不推荐使用
i = sa.pop()
print(i, sa)  # 1 {2, 3, 4, 5, 6, 7, 8, 9, 10}

# - 集合的数学操作：交集，差集，并集，补集
# -- intersection 交集
sa = {1, 2, 3, 4, 5, 6}
sb = {4, 5, 6, 7, 8, 9}
print(sa.intersection(sb))  # {4, 5, 6}
print(sa & sb)  # {4, 5, 6}
# -- difference 差集
print(sa.difference(sb))  # {1, 2, 3}
print(sa - sb)  # {1, 2, 3}
# -- union 并集
print(sa.union(sb))  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
# -- 补集
print(sb - sa)  # sa 的补集 {8, 9, 7}
# -- 异或
print(sa ^ sb)  # {1, 2, 3, 7, 8, 9}
# -- frezonset 冻结
sb = frozenset(sa)
print(sa)  # {1, 2, 3, 4, 5, 6}
print(sb)  # frozenset({1, 2, 3, 4, 5, 6})
