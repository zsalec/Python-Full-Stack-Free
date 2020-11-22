# 程序结构
# - 顺序
# - 分支
# - 循环

# - 分支
# -- if 条件表达式:
# --    语句块
age = 17
if age < 18:
    print('去叫家长')
    print('我们不带你玩')
    print('滚球去')

# -- 双分支
gender = input('请输入性别')
if gender == '男':
    print('代码敲10遍')
else:
    print('给你糖吃')
print('开始上课')

# -- 多分支
# --- elif 可又有多个，没有限制
s = input('请输入分数')
score = int(s)
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('E')
    print('我没有你这样的学生')

# if 语句其他：
# - if 语句可以嵌套，但不推荐
# - Python 没有 switch case 语句
# - 用 {case: func,...}.get(case, default) 代替

# 循环语句
# - for
# - while

# - for 循环
# -- for 变量 in 序列:
# --    语句块
for name in ['Tommy', 'Jerry', 'Mickey']:
    print('name: ', name)
    if name == 'Jerry':
        print('You a rate')
    else:
        print('What are you?')
else:
    print('It is Disney')
'''
name:  Tommy
What are you?
name:  Jerry
You a rate
name:  Mickey
What are you?
'''

# - range 介绍
# -- * 左包含，右不包
for i in range(1, 10):
    print(i)
'''
1
2
3
4
5
6
7
8
9
'''

# -- for-else 语句
# --- 当 for 循环语句结束的时候，运行 else 语句
# --- else 语句是可选语句

# -- 循环变量取名：如果没有使用，可以用 _
for _ in range(1, 11):
    print('I love Python')

# -- break, continue, pass

# --- break
for i in range(1, 11):
    if i == 7:
        print('Found')
        break
    else:
        print(i)  # print 1-6

# --- continue
for i in range(1, 11):
    if i % 2 == 1:
        continue
    else:
        print('{} is even number'.format(i))  # print event
# ------------------
for i in range(1, 11):
    if i % 2 == 0:
        print('{} is even number'.format(i))
# ------------------
for i in range(1, 11):
    if i % 2 == 1:
        continue
    print('{} is even number'.format(i))

# --- pass 占位
for i in range(1, 11):
    pass
