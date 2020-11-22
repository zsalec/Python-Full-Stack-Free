# 变量作用域
# - 分类
# -- 全局变量 global
# -- 局部变量 local
a1 = 100


def func():
    print(a1)
    print('I am in func')
    a2 = 99
    print(a2)
    return None


print(a1)  # 100
func()
'''
100
I am in func
99
'''
# - 不能访问函数内部变量
# print(a2)
'''
Traceback (most recent call last):
  File "C:/Works/learn/python/prime/Chapter3/3-4-scope-list.py", line 17, in <module>
    print(a2)
NameError: name 'a2' is not defined
'''

b1 = 10


def func2():
    global b1
    b1 = 100
    print('func2: b1 = {}'.format(b1))
    print('I am in func2')
    b2 = 99
    print(b2)
    return None


print('b1 = {}'.format(b1))  # b1 = 10
print('-' * 20)
func2()
'''
func2: b1 = 100
I am in func2
99
'''
print('-' * 20)
print('b1 = {}'.format(b1))  # b1 = 100

# - globals, locals
a = 1
b = 2


def func3():
    e = 111
    print('-' * 80);
    print('locals: {}'.format(locals()))
    # print locals
    print('global: {}'.format(globals()))
    return None


func3()
'''
--------------------------------------------------------------------------------
locals: {'e': 111}
global: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000000001DBCE48>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:/Works/learn/python/prime/Chapter3/3-4-scope-list.py', '__cached__': None, 'a1': 100, 'func': <function func at 0x00000000024E4438>, 'b1': 100, 'func2': <function func2 at 0x00000000024E44C8>, 'a': 1, 'b': 2, 'func3': <function func3 at 0x0000000001E0C708>}
'''

# - eval() 函数
# -- 有返回值
x = 10
y = 20
z = eval('x+y')
print('eval("x+y"): {}'.format(z))  # eval("x+y"): 30

# exec() 函数
# -- 无返回值
z = exec('x+y')
print('exec("x+y"): {}'.format(z))  # exec("x+y"): None

# 递归函数 recurrent
# -- 对递归深度有限制
x = 0


def recurrent():
    global x
    x += 1
    print('x={}'.format(x))
    recurrent()
    return None


try:
    recurrent()
except RecursionError as e:
    print(e)  # maximum recursion depth exceeded while calling a Python object
    print('deep: {}'.format(x))  # deep: 997
else:
    print('error')


# fibonnaci
def fibonnaci(number):
    if number < 1:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonnaci(number - 1) + fibonnaci(number - 2)


for num in range(1, 11):
    print('fibonnaci({}): {}'.format(num, fibonnaci(num)))
'''
fibonnaci(1): 1
fibonnaci(2): 1
fibonnaci(3): 2
fibonnaci(4): 3
fibonnaci(5): 5
fibonnaci(6): 8
fibonnaci(7): 13
fibonnaci(8): 21
fibonnaci(9): 34
fibonnaci(10): 55
'''

# 内建数据结构（变量类型）
# - list
# - set
# - tuple
# - dict

# - list
# -- 有序
l1 = []
print(type(l1))
print(l1)
'''
<class 'list'>
[]
'''

l2 = [100]
print(type(l2))
print(l2)
'''
<class 'list'>
[100]
'''

l3 = [1, 3, 2, 4, 5]
print(type(l3))
print(l3)
'''
<class 'list'>
[1, 3, 2, 4, 5]
'''

l4 = list()
print(type(l4))
print(l4)
'''
<class 'list'>
[]
'''
l5 = list([1, 2, 3])
print(type(l5))
print(l5)
'''
<class 'list'>
[1, 2, 3]
'''

# -- 列表常用操作
# --- 访问
# ---- 使用下标
# ---- 从 0 开始
l = [2, 2, 3, 4, 1, 5]
print(l[0])  # 2

# --- 分片操作
# ---- 左包含，右不包含
print(l[1:3])  # [2, 3]
# ---- 如果不写
# ----- 左边：为 0
# ----- 右边：结尾
# ----- 步长：1
# ---- 下标可以超出范围。但不会报错
# ---- 可以为负数。负数表示从右边数，但是方向不变，从左往右
# ---- 步长为负的时候，表示反向截取
print(l[1:])  # [2, 3, 4, 1, 5]
print(l[:3])  # [2, 2, 3]
print(l[::2])  # [2, 3, 1]
print(l[3:100])  # [4, 1, 5]
print(l[-3:-1])  # [4, 1]
print(l[-3:0])   # []
print(l[-3:])   # [4, 1, 5]
print(l[-1:-4:-1])  # [5, 1, 4]
print(l[-3::-1])  # [4, 3, 2, 2]
# ---- 切片生成新的列表 list
print(id(l), id(l[1:2]))  # 39140936 39140872
print(id(l), id(l[:]), 'id(l)==id(l[:]) is {}'.format(id(l) == id(l[:])))  # 39010248 34723208 id(l)==id(l[:]) is False

# -- id 函数
# --- * 变量只是一个指向内存数据的地址
a = 100
b = 200
print(id(a), id(b), 'id(a)==id(b):{}'.format(id(a) == id(b)))  # 8791431740768 8791431743968 id(a)==id(b):False
c = a
print(id(a), id(c), 'id(a)==id(c):{}'.format(id(a) == id(c)))  # 8791431740768 8791431740768 id(a)==id(c):True
a = 101
print(id(a), id(b), 'id(a)==id(b):{}'.format(id(a) == id(b)))  # 8791431740800 8791431743968 id(a)==id(b):False
print(id(a), id(c), 'id(a)==id(b):{}'.format(id(a) == id(c)))  # 8791431740800 8791431740768 id(a)==id(b):False
a = 200
print(id(a), id(b), 'id(a)==id(b):{}'.format(id(a) == id(b)))  # 8791431743968 8791431743968 id(a)==id(b):True
