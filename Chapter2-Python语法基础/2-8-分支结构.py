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
# - 语法结构
# if 条件表达式:
#   语句块1
# else:
#   语句块2
a = 'Everyone buy my classes'
if a:   # 字符串为空 - False，否则 - True
    print('I will become a rich-man!')
    print('To marry a BAI-FU-MEI girl')
else:
    print('Keep you level!')
print('I have to go on with my life!')

# demo
# input 的作用是
# 1. 在屏幕上输出括号内的字符串
# 2. 接收用户输入的内容病返回到程序
# 3. input 返回的内容一定是字符串类型
print('Please input your gender: ')
gender = input()
print(gender)
if gender == 'man':
    print('Go to drinking, cutting head')
    print('Playing together moment')
else:
    print('Who are you?')
    print('Sorry, I am a boy!')

# 考试成绩判断
# 成绩由用户输入
# 90以上：输出优秀
# 80-90: 良
# 70-80: 中
# 60-70: 平
# 60 以下：输出：我没你这傻学生
score = int(input('请输入考试成绩：'))
if score >= 90:
    print('优秀')
elif score >=80:
    print('良')
elif score >= 70:
    print('中')
elif score >= 60:
    print('平')
else:
    print('我没你这傻学生')