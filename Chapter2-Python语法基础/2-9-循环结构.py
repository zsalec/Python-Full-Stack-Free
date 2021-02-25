# 分支结构 demo (branch demo)
# 考试成绩判断
# 成绩由用户输入
# 90 以上：输出 优秀
# 80-90：良
# 70-80：中
# 60-70：平
# 60 以下：没有你这个学生
score = input('Please input your score: ')
score = int(score)
if score >= 90:
    print('优秀')
if (score >= 80) and (score < 90):
    print('良')
if (score >= 70) and (score < 80):
    print('中')
if (score >= 60) and (score < 70):
    print('平')
if score < 60:
    print('You are not my student!')

# 多路分支
# - 很多分支的情况，叫多路分支
# if 条件1:
#   语句块1
# elif 条件2:
#   语句块2
# ...
# else:
#   语句块n
score = input('Please input your score: ')
score = int(score)
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('You are not my student!')

# if 语句补充
# if 语句可以嵌套使用，（不推荐）
# Python 没有 switch 语句

# 循环语句
# - 重复执行某一个固定的动作或者任务
# - 分类
# - while
# - for

# for 循环
# - 语法
#   for 变量 in 序列:
#       语句块

# for 案例
list_one = [1, 2, 3, 4, 5, 6, 7]
for num in list_one:
    print(num)
    print(num + 100)
    print(num + 1000)

# for - else
stu_list = ['Tom', 'Jerry', 'White', 'William', 'Bush']
for name in stu_list:
    if name == 'Bush':
        print(name + ', you will be President')
    else:
        print('I donot know you ' + name)
else:
    print('It is over.')

# break, continue, pass
# - break: unconditional end for-cyclic, short for suddenly dead
dig_list = [3, 4, 5, 6, 22, 33, 7, 5, 43]
for dig in dig_list:
    if dig == 7:
        print('HA~HA~, got it')
        break
    else:
        print(dig)
