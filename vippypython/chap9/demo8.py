# 字符串的常用操作

# 替换字符串 replace
s = 'hello, Python'
print(s.replace('Python', 'Java'))

s1 = 'hello, Python, Python, Python'
print(s1.replace('Python', 'Java', 2))

# 拼接字符串 join
lst = ['hello', 'java', 'python']
print('|'.join(lst))

t = ('hello', 'Java', 'Python')
print('-'.join(t))

print('*'.join('Python')) # P*y*t*h*o*n