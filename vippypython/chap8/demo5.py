# 集合的创建方式
# 集合中的元素不能重复

# 1. 使用花括号 {}
s = {2,3,4,5,5,6,7,7}
print(s, type(s)) # type: set

# 2. 内置函数 set()
s1 = set(range(6))
print(s1, type(s1))

# 列表去重
s2 = set([1,2,3,4,5,5,5,6,6])
print(s2, type(2))

# 集合是无序的
s3 = set((1,2,4,4,5,65))
print(s3, type(s3))

s4 = set('Python')
print(s4, type(s4))

s5 = set({1,2,3,34,4,40,4,78})
print(s5, type(s5))

# 定义一个空集合
s6 = {} # !字典 type: dict
print(type(s6))

s7 = set()
print(type(s7)) # type: set