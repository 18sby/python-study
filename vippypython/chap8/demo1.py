# 不可变序列（数据结构的id是不变的） vs 可变序列（数据结构更改后内存地址发生了更改）

# 可变序列 列表、字典
lst = [10,20,45]
print(id(lst))
lst.append(300)
print(id(lst))

# 不可变序列 字符串、元组，不能执行增删改
s = 'hello'
print(id(s))
s = s + ' world'
print(id(s))