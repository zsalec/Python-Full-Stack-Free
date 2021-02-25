"""
# str 字符串
- str
- 转义字符
- 格式化
- 内建函数
"""

# 字符串
# - 单引号，双引号，三引号

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

'''
# 转义字符
- 用一个特色的方法表示出一系列不方便写出的内容，比如回车键，换行符，退格符
- 借助反斜杠字符，一旦字符串中出现反斜杠，则反斜杠后面一个或几个字符表示已经不是原来的意思了，进行转移
- 在字符串中，一旦出现反斜杠就要加倍小心，可能有转义字符出现
- 不同系统对换行符操作有不同的表示
    - Windows: \n
    - Linux: \r\n
'''

# 转义字符的案例
s = 'Let\'s go'
print(s)

# 使用单双引号嵌套
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

'''
# 常用转义符
- \ 表示此行未结束
- \\ 反斜杠
- \' 单引号
- \" 双引号
- \a 响铃
- \b 退格
- \e 转移
- \000 空
- \n 换行
- \v 纵向制表符
- \t 横向制表符
- \r 回车
- \f 分页符
- \oyy 八进制
- \xyy 十六进制
- \other 其他
'''

# 格式化
# - 把字符串按照一定格式进行打印或者填充
# - 格式化的分类
#   - 传统格式化
#   - format

# 填充
# 字符串的传统格式化方法
# - 使用 % 进行格式化
# - %（百分号）也叫占位符
#   - %s 字符串
#   - %r 字符串，但是是使用 repr 而不是 str
#   - %c 整数转换为单个字符
#   - %d 十进制数
#   - %u 无符号整数
#   - %o 八进制
#   - %x 十六进制（小写）
#   - %X 十六进制（大写）
#   - %e 浮点数（e 小写）
#   - %E 浮点数（E 大写）
#   - %f，%F 浮点数
#   - %g，%G 十进制形式浮点或者指数浮点自动转换
#   格式字符前出现整数表示此占位符所占位置的宽度
#   格式字符前面出现‘-’表示左对齐
#   格式字符前面出现‘+’表示右对齐
#   width表示宽度
#   precision 精度

# 案例
s = 'I love %s'
print(s)  # I love %s
print(s % 'Python')  # I love Python
print(s % 'C++')  # I love C++

s = 'I am %.1fkg, %.2fcm'
print(s % (73.4, 1.70))
