class A:
    pass


class B(A):
    pass


# 子类在前，父类在后
# 不推荐，建议舍弃
class C(B, A):
    pass


print('A.__mro__:', A.__mro__)
print('B.__mro__:', B.__mro__)
print('C.__mro__:', C.__mro__)
'''
A.__mro__: (<class '__main__.A'>, <class 'object'>)
B.__mro__: (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
C.__mro__: (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
'''