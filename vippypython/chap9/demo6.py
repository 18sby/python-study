# 字符串的分割操作，类似 js，分割的结果是列表(js Array)

# 默认使用空格分割
s = 'hello world python'
lst = s.split()
print(lst)

# 使用指定符号分割
s1 = 'hello|world|python'
print(s1.split(sep="|"))

# 指定最大分割次数
print(s1.split(sep="|", maxsplit=1))

# rsplit() 从右侧开始分割
print(s.rsplit())
print(s1.rsplit(sep='|'))
print(s1.rsplit(sep="|", maxsplit=1))