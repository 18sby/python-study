# 赋值运算符
i = 3 + 4
print(i)

# 链式赋值 id 是一样的
a = b = c = 20
print(a, id(a))
print(b, id(b))
print(c, id(c))

print('\n-----支持参数赋值-----\n')

a = 20
a += 30 # a = a + 30
print(a)

a -= 10 # a = a - 10
print(a)

a *= 2 # a = a * 2
print(a)

a /= 3 # a = a / 3
print(a)

a //= 2
print(a)

a %= 3
print(a)

print('\n-----系列解包赋值-----\n')

a,b,c = 20,30,40
print(a, b, c)
# 交换两个变量的值
a,b = b,a
print(a, b, c)