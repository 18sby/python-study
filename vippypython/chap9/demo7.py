# isidentifier() 判断字符串是否为合法字符
s = 'hello, python'
print('1.', s.isidentifier())
print('2.', 'hello'.isidentifier())
print('3.', '张三_'.isidentifier())
print('4.', '张三__123'.isidentifier())

# isspace() 是否为空白字符
print('5.', '\t'.isspace())

# isalpha() 是否为字母组成
print('6.', 'abc'.isalpha())
print('7.', '张三'.isalpha())
print('8.', '张三1'.isalpha())

# isdecimal() 是否为十进制数字组成
print('9.', '123'.isdecimal())
print('10.', '123四'.isdecimal())

# isnumeric() 是否为数字组成
print('11.', '123'.isnumeric())
print('12.', '123四'.isnumeric())

# isalnum() 是否为字母数字
print('13.', 'abc1'.isalnum())
print('14.', '张三1231'.isalnum())