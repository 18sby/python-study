# 输出字符串和数字
print('hello python')
print(520)

# 含有运算符的表达式
print('3'+'1')
print(3+1)

# 将数据输出到文件中
# a+: 没有则会创建，有文件，就会在原文件内容后面追加
# 1. 所指定的盘符存在
# 2. print 时候使用 file=fp，不然写不进去内容
# fp = open('/Users/a/sby/studyLesson/blbl/python/python-study/vippypython/files/first.txt', 'a+')
# print('hellow python3', file=fp)
# fp.close()

# 不进行换行输出（输出内容是在一行）
print('hello', 'world', 'Pyhton')