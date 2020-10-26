# 元组的创建方式

# 第一种: () 可以省略小括号
t = ('Python', 'world', 98)
print(t, type(t)) # type: tuple

t2 = 'Python', 'world', 99
print(t2, type(t2))

# 如果元组中只有一个元组，要加上逗号，不然会被认为是 str|int 类型
t3 = 'Python',
print(t3, type(t3))

# 第二种: 内置函数 tuple()
t1 = tuple(('Python', 'hello', 100))
print(t1, type(t1))


# 空元组的创建方式
t4 = ()
t5 = tuple()
print('空元组', t4, t5)

# 空列表的创建方式
lst = []
lst1 = list()
print('空列表', lst, lst1)

# 空字典
d = {}
d2 = dict()
print('空字典', d, d2)