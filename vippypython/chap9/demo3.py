# 字符串的查询操作

s = 'hello,hello'
print(s.index('lo'))
print(s.find('lo'))
print(s.rindex('lo'))
print(s.rfind('lo'))

# print(s.index('k')) # 会报错
print(s.find('k')) # -1，推荐这个