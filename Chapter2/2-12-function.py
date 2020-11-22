# 函数的参数和返回值
# - 参数：负责给函数传递一些必要的数据或者信息
# -- 形参（形式参数）：没有具体值，只是一个占位符
# -- 实参（实际参数）：调用函数的时候输入的值

# person - 形参
def hello(person):
    print('Hello, {0}'.format(person))
    print('{0}, did you see Tom?'.format(person))
    return None


# p - 实参
p = 'William'
hello(p)
print()
p = 'Bush'
hello(p)
print()

# - 返回值：调用函数的时候的一个执行结果。可选的
# -- 用 return 返回结果
# -- 如果没有值需要返回，推荐使用 return None 表示函数结束
# -- 如果函数没有 return 关键字，函数默认返回 None
pp = hello('John')
print(pp)
print()

# help 负责随时提供帮助
help(print)


# 九九乘法表
# 明确循环次数，用 for 循环
def table99():
    for r in range(1, 10):
        for c in range(1, r + 1):
            print('{0} * {1} = {2}'.format(c, r, c * r), end='\t')
        print()
    return None


table99()
