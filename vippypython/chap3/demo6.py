# 布尔运算符

a,b = 1,2
print('\n----- and && -----\n')
print(a == 1 and b == 2) # True
print(a == 1 and b < 2) # False
print(a != 1 and b == 2) # False
print(a != 1 and b != 2) # False

print('\n----- or || -----\n')
print(a == 1 or b == 2)
print(a == 1 or b < 2)
print(a != 1 or b  == 2)
print(a != 1 or b != 2)

print('\n----- not ! 对 bool 类型的操作数取反 -----\n')

f = True
f2 = False
print(not f)
print(not f2)

print('\n----- in 与 not in -----\n')
s = 'hello world'
print('w' in s)
print('k' in s)
print('w' not in s)
print('k' not in s)