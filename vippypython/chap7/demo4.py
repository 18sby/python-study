score = { '张三': 100, '李四': 98, '王五': 99 }

# 获取所有的键
keys = score.keys()
print(keys, type(keys)) # type: dict_keys

print(list(keys), type(list(keys)))

# 获取所有的值
values = score.values()
print(values, type(values)) # type: dict_values

print(list(values))

# 获取所有的键值对
items = score.items()
print(items, type(items)) # type: dict_items
print(list(items), type(list(items))) # 元组