# - continue
# find even
dig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for dig in dig_list:
    if dig % 2 == 1:
        continue
    print(dig)
    print('HA~HA~')

# - pass 占位符
age = 19
if age > 19:
    pass
else:
    print('You are too younger')

ages = [2, 23, 43, 54, 65, 2]
for age in ages:
    pass
    print(age, end=' ')
print()

# range 函数
# - 生成有序数列
# ** 左包括，右不包括
dig_list = range(1, 10)
for dig in dig_list:
    print(dig, end=' ')
print()

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
