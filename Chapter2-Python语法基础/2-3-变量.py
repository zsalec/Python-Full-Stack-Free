"""
# 主要内容
- 坚持写 Blog
- jupyter notebook 的用法
- 变量
- 跟 vi/vim 的编辑模式很像
"""

# 声明变量的三种格式
# 格式 1
s1 = 'I love Python'

# 格式 2
s1 = s2 = 'I love Python'

# 格式 3
s1, s2, s3 = 'I love Python', 'I love China', 'Thinking less, done more'

print('I love Python')

"""
# 变量类型
- 严格意义上讲，Python 只有一种类型
- 标准数据类型六种
# 1. 数字 Number
# 2. 字符串 String
# 3. 列表 list
# 4. 元组 tuple
# 5. 字典 dict
# 6. 集合 set
"""

"""
# 数字类型 Number
- Python 中的数字类型没有大小限制
# 常见数字分类
- 整数
    - 没有小数部分
    - 包含正数，负数，0
    - 二进制
        - 只有 0 1
        - 以 0b 开头的 01 串
        - 例如：
            - 0b110
            - 0b11110
    - 八进制
        - 以 0o 开头的 0 到 7 之间的数字串
        - 例如：
            - 0o71
    - 十六进制
        - 以 0x开头，由 0-9, a-f 构成的串

- 浮点数
- 科学计数法
- 复数 Complex
"""

# 二进制
a1 = 0b110
print(a1)  # 6

a2 = 0b1110
print(a2)  # 30

# 八进制
a3 = 0o71
print(a3) # 57

# 十六进制
a4 = 0xffff
print(a4) # 65535
a5 = 0x53f2
print(a5) # 21490

a5 = 0x83f2
print(a5) # 33778
