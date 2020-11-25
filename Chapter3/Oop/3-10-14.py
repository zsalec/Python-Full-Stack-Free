# 构造函数的调用顺序 - 2
# 如果子类没有写构造函数，则自动向上查找，直到找到为止
class A:
    def __init__(self):
        print('A')
        return None


class B(A):
    def __init__(self):
        print('B')
        return None


class C(B):
    pass


# 此时，首先查找 C 的构造函数
# 如果没有，则向上安装 MRO 顺序查找父类的构造函数，直到找到为止
c = C()  # B
