# 转义字符

# \n 换行
print('hello\nworld')

# /t 一组四个空格 !:是四位四位地来计算
print('hello\tworld')

# \r 回车   world 将 hello 进行了覆盖
print('hello\rworld')

# \b 退格，退一个格
print('hello\bworld')

print('http://www.baidu.com')
print('老师说: \'大家好\'')

# 原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上 r 或者 R
# 注意：最后一个字符不能是反斜线
print(r'hello\nworld')