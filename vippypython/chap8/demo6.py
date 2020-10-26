# 集合的相关操作

s = { 10, 20, 30, 40, 50 }

# 判断操作
print(10 in s)
print(100 in s)
print(15 not in s)

# 新增操作

# set.add() 添加一个元素
s.add(60)
print(s)

# set.update(iterator) 传一个可迭代对象，全部添加到集合当中  一次至少添加一个元素
s.update(range(100,110))
print(s)

s.update([1000,2000])
print(s)

# 删除操作
s.remove(100) # 元素不存在会报错
s.discard(500) # 元素不存在也不会报错
print(s)
s.pop() # 删除一个任意元素
s.pop()
print(s)
s.clear() # 清空集合的所有元素
print(s)