"""
# 字符串
- 表达文字信息的内容，比如 'I love Python'
- 形式上是引号引起来的一段内容
- 引号包括
    - 单引号
    - 双引号
    - 三引号，可以用来表示多行信息
- 单双引号含义一致

# 单双引号只能表示一行信息
# 三引号可以表示多行信息
"""

love = 'Ich liebe Python'
print(love)

love1 = 'I love Python'
print(love1)

love2 = "I love my family."
print(love2)

love3 = '''
I
Love
You
China
Like loving nothern-snow

My native-country
'''
print(love3)

'''
# 以下案例说明单双引号只能引用一行
love4 = "
I
Love you
China
like loving northern-snow
"
'''

'''
# None 类型
- 表示没有，通常用来表示占位
- 比如返回，用来表示返回一个空
# 都用于函数返回
'''
