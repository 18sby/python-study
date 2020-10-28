# 字符串常用的对齐操作

s = 'hello, Python'

# 居中对齐填充
print(s.center(20, '*')) # ***hello, Python****

# 左对齐
print(s.ljust(20, '*'))
print(s.ljust(10))
print(s.ljust(20)) # 默认填充符是空格

# 右对齐
print(s.rjust(20, '*'))
print(s.rjust(20))
print(s.rjust(10))

# 右对齐，使用 0 进行填充
print(s.zfill(20))
print(s.zfill(10))
print('-8910'.zfill(8)) # 0 会被填充到减号后边