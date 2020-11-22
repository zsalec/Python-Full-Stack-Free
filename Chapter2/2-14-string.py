# 字符串
# 单引号，双引号，三引号

# - 单引号
s = 'Hello world'
print(s)

# - 双引号
s1 = "Hello, python"
print(s1)

# - 三引号
s = """
I
Love
My
Native-Country,
China
"""
print(s)

# 转义字符
s = 'Let\'s go'
print(s)

# 引号嵌套
s = "Let's Go"
print(s)

# 表示路径
s = 'c:\\users\\administrator'
print(s)

# 换行转义
# 代码换行
s = 'A Grain of Sand\nWilliam Blake\nTo see a world in a grain of sand,\nAnd a heaven in wild flower,\nHold infinity ' \
    'in the palm of your hand,\nAnd eternity in an hour.'
print(s)

# 格式化
# 填充
s = 'I love %s'
print(s)  # I love %s
print(s % 'Python')  # I love Python
print(s % 'C++')  # I love C++

s = 'I am %.1fkg, %.2fcm'
print(s % (73.4, 1.70))
