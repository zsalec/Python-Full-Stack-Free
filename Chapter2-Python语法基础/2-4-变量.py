"""
# 浮点数
- 就是通俗意义上的小数
- 常见的案例格式
    - 3.1415926
    - 3.
    - 0.4
    - .4
- 科学计数法
    - 定义跟数学定义一致
    - 写法就是 e 后面跟整数用来表示 10 的指数
"""

# 浮点数
# 科学计数法

height = 184
print(height)

height = 1.84e2
print(height)

a = .2
print(a)

"""
# 复数 complex
- 与数字定义一致
- 复数的虚部用 /J 表示
- 例如：
    - 5+4j
    - 4j
    -(4j)
"""

a = 4j
print(a)

"""
# 布尔值
- 布尔值就是用来表示真假的值
- 只有两个值：True/False
- 在 Python 中，布尔值可以当数字使用
    - 布尔值可以作为数字使用，True=1，False=0
    - 数字也可以作为布尔值。0=False，非零=True
"""

age = 18 + True
print(age)  # 19
age = 18 + False
print(age)  # 18

a = -1
if a:
    print("minus is True")
else:
    print("minus if False")
# minus is True
