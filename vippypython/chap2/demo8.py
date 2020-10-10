name = '张三'
age = 20

print(type(name), type(age))

# str 和 int 类型不能连接，需要转换
print('我叫' + name + '今年' + str(age) + '岁')

print('\n------ str() 将其他类型转成 str 类型------\n')
a = 10
b = 198.8
c = False
print(type(a), type(b), type(c))
print(str(a), str(b), str(c))
print(str(a) + str(b) + str(c))
print(type(str(a)), type(str(b)), type(str(c)))

print('\n------ int() 将其他类型转成 int 类型------\n')
s1 = '128'
f1 = 98.7
s2 = '76.25'
ff = True
s3 = 'hello'
print(type(s1), type(f1), type(s2), type(ff), type(s3))
print(int(s1), type(int(s1)))
print(int(f1), type(int(f1)))
# print(int(s2), type(int(s2))) # 将 str 转成 int 类型，报错，因为字符串为小数串
print(int(ff), type(int(ff)))
# print(int(s3), type(int(s3))) # 将 str 转成 int 类型，字符串必须为数字串（整数），非数字串是不能转换的

print('\n------ float() 将其他类型转成 float 类型------\n')
s1 = '128.985'
s2 = '76'
ff = True
s3 = 'hello'
i = 98
print(type(s1), type(s2), type(ff), type(s3), type(98))
print(float(s1), type(float(s1)))
print(float(s2), type(float(s2)))
print(float(ff), type(float(ff)))
# print(float(s3), type(float(s3))) # 字符串中的数据如果是非数字串，则不允许转换
print(float(i), type(float(i)))