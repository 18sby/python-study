# 字符串切片

# 切片[start:end:step] 默认[0:字符串的长度:1]

s = 'hello,python'

# 未指定起始位置，从 0 开始截取
s1 = s[:5]

# 没有指定结束位置，会切到字符串的最后一个元素
s2 = s[6:]

s3 = '!'
newStr = s1 + s3 + s2
print(newStr) # hello!python

print(id(s1))
print(id(s2))
print(id(s3))
print(id(newStr))

print('\n-----\n')

# 从索引 1 开始，到 5 之前，步长为 1
print(s[1:5:1]) # ello

print(s[::2]) # hlopto

# 倒序，有翻转字符串的效果，步长为负数，向左
print(s[::-1])

print(s[-6::1]) # python