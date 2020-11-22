# 程序结构
# - 顺序
# - 循环
# - 分支

# 分支结构 - if
# - 条件必须是布尔值得表达式
# - 表达式后面的冒号不能少
# - 注意 if 后面出现的语句。如果属于 if 语句块，则必须同一个缩进等级
# - 条件表达式的结果为 True，则执行 if 后面的缩进语句块
a = 'Everyone buy my classes'
if a:   # 字符串为空 - False，否则 - True
    print('I will become a rich-man!')
    print('To marry a BAI-FU-MEI girl')
print('I have to get on with my life!')

age = 19
if age > 16:
    print('Go to drinking')
print('You will invest me next time')

# 双向分支
a = 'Everyone buy my classes'
if a:   # 字符串为空 - False，否则 - True
    print('I will become a rich-man!')
    print('To marry a BAI-FU-MEI girl')
else:
    print('Keep you level!')
print('I have to get on with my life!')

# demo
print('Please input your gender: ')
gender = input()
print(gender)
if gender == 'man':
    print('Go to drinking, cutting head')
    print('Playing together moment')
else:
    print('Who are you?')
    print('Sorry, I am a boy!')
