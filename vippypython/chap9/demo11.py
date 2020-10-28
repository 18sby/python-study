# 格式化字符串

# 1. % 占位符
name = '张三'
age = 24
print('我叫%s，今年%d岁了' % (name, age)) # 我叫张三，今年24岁了

# 2. {0} 0 带表索引
print('我叫{0}，我{1}岁了，我真的是{0}'.format(name, age))\

# 3. f-string
print(f'我叫{name}，今年{age}岁了')