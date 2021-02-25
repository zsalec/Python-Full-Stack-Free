# 组装类例子 2
# 自己组装一个类
from types import MethodType


class A:
    pass


def say(self):
    print('Say......(from function)')
    return None


a = A()
# 组装类方法
a.say = MethodType(say, A)
a.say()  # Say......(from function)
