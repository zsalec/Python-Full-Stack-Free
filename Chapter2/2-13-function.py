# 函数的嵌套
# 九九乘法表
# 明确循环次数，用 for 循环
def table99():
    def printLine(line_num):
        """
        打印一行九九乘法表
        :param line_num: 行号
        :return: None
        """
        for c in range(1, line_num + 1):
            print('{0} * {1} = {2}'.format(c, line_num, c * line_num), end='\t')
        print()
        return None

    for r in range(1, 10):
        printLine(r)
    return None


table99()
table99()


# 参数详解
# - 普通参数
# - 默认参数
# - 关键字参数
# - 收集参数


# 普通参数
def normal_param(one, two, three):
    print(one + two)
    return None


normal_param(1, 2, 3)  # 3


# 默认参数
def default_param(one, two, three=100):
    print(one + two)
    print('three = {0}'.format(three))
    return None


default_param(1, 2)  # 3     100
default_param(1, 2, 3)  # 3     6


# 关键字参数
def keys_param(one, two, three):
    print(one + two)
    print(three)
    return None


keys_param(one=1, two=2, three=3)  # 3     3
keys_param(two=2, three=3, one=10)  # 12     3
