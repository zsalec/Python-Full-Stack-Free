"""
# Continue, Break, Pass
- break：无条件结束整个循环，简称循环猝死
- continue：继续
- pass：只是占位符号，代表这句话啥也不干，没有跳过功能
"""

# - continue 语句练习
# find even
dig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
continue 案例1
'''
for dig in dig_list:
    if dig % 2 == 0:
        print(dig)
        print('haha, it is even')
# 此段代码与上面的大妈等价
for dig in dig_list:
    if dig % 2 == 1:
        continue
    print(dig)
    print('HA~HA~')

# - pass 占位符
# pass 案例 1
age = 19
if age > 19:
    pass
else:
    print('You are too younger')
# pass 案例 2
ages = [2, 23, 43, 54, 65, 2]
for age in ages:
    pass
    print(age, end=' ')
print()

# range 函数
# - 生成有序数列
# ** range 生成的序列的数字是：左包括，右不包括
# - 一般在 python 中，表示范围的数字都是左包括，右不包括。randint 函数是个例外
# - range 函数在 python2.x 和 python3.x 有很大区别
dig_list = range(1, 101)
for dig in dig_list:
    print(dig, end=' ')
print()
'''
# range 案例 3
- 打印从 1 到 9 的数字
'''
for i in range(1, 10):
    print(i)

# while 循环
# - 条件成立时执行循环
# - 适用于不确定具体循环次数
principle = 100
interest = 0.06
year = 0
while principle < 200:
    principle *= 1 + interest
    year += 1
print('After ' + str(year) + ' years, your principle is more than 200')

# while - else
principle = 100
interest = 0.06
year = 0
while principle < 200:
    principle *= 1 + interest
    year += 1
else:
    print('After ' + str(year) + ' years, your principle is more than 200')
