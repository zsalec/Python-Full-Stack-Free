# 构造函数的调用顺序 - 3
# 如果子类没有写构造函数，则自动向上查找，直到找到为止
class A:
    def __init__(self):
        print('-' * 20)
        print('A.__init__')
        print('A')
        print('*' * 10, 'End of A.__init__')


class B(A):
    # 第二种方法：通过 super 调用
    def __init__(self, name):
        # 首先调用父类构造函数
        print('-' * 20)
        print('B.__init__')
        super(B, self).__init__()
        # 其次，再增加自己的功能
        print('B')
        print(name)
        print('*' * 10, 'End of B.__init__')



class C(B):
    # C 中想扩展 B 的构造函数
    # 即调用 B 的构造函数后在添加一些功能
    # 有两种方法实现
    # 第一种方法：通过父类名调用
    def __init__(self, name):
        # 首先调用父类构造函数
        print('-' * 20)
        print('C.__init__')
        B.__init__(self, name)
        # 其次，再增加自己的功能
        print('这是 C 中附加的功能')
        print('*' * 10, 'End of C.__init__')


# 此时，首先查找 C 的构造函数
# 如果没有，则向上安装 MRO 顺序查找父类的构造函数，直到找到为止
try:
    c = C('我是 C')  # B
except TypeError:
    print("TypeError: __init__() missing 1 required positional argument: 'name'")
'''
--------------------
C.__init__
--------------------
B.__init__
--------------------
A.__init__
A
********** End of A.__init__
B
我是 C
********** End of B.__init__
这是 C 中附加的功能
********** End of C.__init__
'''