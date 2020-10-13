# range() 内置函数

# 第一种方式 range(stop)
r = range(20) # 0 - 19，20 个整数，默认从零开始，步长为1
print(list(r))

# 第二种方式 range(start, stop)
r = range(1, 5)
print(list(r))

# 第三种方式 range(start, stop, step)
r = range(10, 30, 5)
print(list(r))

# 判断指定的整数，在序列中是否存在 in, not in
print(10 in r)
print(11 not in r)