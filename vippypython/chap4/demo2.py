# 测试对象的布尔值

print('-----这些对象的布尔值都是 False-----')
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool(None))
print(bool(''))
print(bool(""))
print(bool([])) # 空列表
print(bool(list()))
print(bool(())) # 空元组
print(bool(tuple())) # 空元组
print(bool({})) # 空字典
print(bool(dict())) # 空字典
print(bool(set())) # 空集合

print('-----其他对象的布尔值都是 True-----')
print(bool(18))
print(bool(True))