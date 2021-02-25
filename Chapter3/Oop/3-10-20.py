# 变量的三种用法
class A:
    def __init__(self):
        self.name = 'haha'
        self.age = 18


a = A()
# 属性的三种用法
# - 赋值
# - 读取
# - 删除
a.name = 'Tonny'
print('a.name:', a.name)
del a.name
try:
    print(a.name)
except AttributeError:
    print("AttributeError: 'A' object has no attribute 'name'")
'''
a.name: Tonny
AttributeError: 'A' object has no attribute 'name'
'''


# 类属性 property
# 应用场景
# 对变量除了普通的三种操作，还想增加一些附加的操作，那么可以通过 property 完成
class B:
    def __init__(self):
        self.name = 'Tonny'
        self.age = 18

    # 此功能，是对类变量进行读取操作的时候，应该执行的函数功能
    def fget(self):
        print('我被读取了')
        return self.name

    # 模拟的是对变量进行写操作的时候执行的功能
    def fset(self, name):
        print('我被写入了，但是还可以做好多事情')
        self.name = name
        return None

    # fdel 模拟的是删除变量的时候进行的操作
    def fdel(self):
        pass

    # property 的四个参数顺序是固定的
    # 第一个参数：读取函数
    # 第二个参数：写入函数
    # 第三个参数：删除操作
    # 第四个参数：描述
    name2 = property(fget, fset, fdel, '这是一个 property 的例子')


b = B()
print('*' * 20)
print('property')
print('b.name:', b.name)
print('b.name2:', b.name2)
'''
********************
property
b.name: Tonny
我被读取了
b.name2: Tonny
'''
