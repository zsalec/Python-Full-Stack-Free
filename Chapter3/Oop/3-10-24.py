# 函数名可以当变量使用
def sayHello(name):
    print('{}，你好，来一发吗？'.format(name))
    return None


sayHello('Tonny')  # Tonny，你好，来一发吗？

rogue = sayHello

rogue('Alice')  # Alice，你好，来一发吗？
