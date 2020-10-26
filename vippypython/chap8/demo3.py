t = (10,[20,30],9)

print(t)
print(type(t))
print(t[0], type(t[0]), id(t[0]))
print(t[1], type(t[1]), id(t[1]))
print(t[2], type(t[2]), id(t[2]))

# 尝试将 t[1] 修改为 100
print(id(100))
# 元组不允许修改元素的
# t[1] = 100

# 由于列表是可变序列，可以向列表中添加元素，而列表的内存地址不变
t[1].append(40)
print(t[1], id(t[1]))