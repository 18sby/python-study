# 字符串大小写转换，不可变序列

s = 'hello, python'

a = s.upper() # 转成大写之后会产生新的字符串
print(a, id(a))
print(s, id(s))

b = s.lower()
print(b, id(b))
print(s, id(s))

print(b == s) # 值相等
print(b is s) # 地址不相等

s2 = 'hello, Python'
print(s2.swapcase()) # 大小写互转，原小写转大写，原大写转小写
print(s2.title()) # 每个单词的首字母大写