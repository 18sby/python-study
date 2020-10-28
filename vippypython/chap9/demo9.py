# 字符串的比较操作

print('apple' > 'app') # True
print('apple' > 'banana') # False
print(ord('a'), ord('b')) # ASCII

print(chr(97), chr(98))
print(ord('🐉'))

'''
  == 与 is 的区别
    ==：比较值
    is：比较 id，也就是内存地址
'''

a = b = 'python'
c = 'python'
print(id(a), id(b), id(c))
print(a == b, a is b)
print(c is b, c == a)