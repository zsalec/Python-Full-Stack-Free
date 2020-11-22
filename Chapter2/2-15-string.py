# format格式化
s = '{} {}!'
print(s)
print(s.format('Hello', 'world'))

# 设置位置
s = '{1}, {0}'.format('world', 'Hello')
print(s)

# 设置名称
s = 'I am {name}, my website is {url}, {teacher} is handsome'
print(s.format(name='Tom', url='http://www.cnczcp.com', teacher='Alec Wang'))

# 数据字典
dic = {'name': 'Tommy',
       'url': 'http://www.cnczcp.com',
       'teacher': 'Alec Wang'}
s = 'I am {name}, my website is {url}, {teacher} is handsome'.format(**dic)
print(s)

# 格式化
s = 'Tommy is {:.2f}m height, {:.2f}kg weight.'
print(s.format(1.7, 73))

# str 内建函数 function build-in
help(str)
help(str.format)