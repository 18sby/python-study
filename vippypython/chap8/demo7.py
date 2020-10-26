# 集合间的关系

# 两个集合是否相等的判断条件：元素相同就相等
s = { 10, 20, 30, 40 }
s2 = { 30, 40, 20, 10 }
print(s == s2)
print(s != s2)

# 集合关系：子集
s1 = { 10, 20, 30, 40, 50, 60 }
s2 = { 10, 20, 30, 40 }
s3 = { 10, 20, 90 }
s4 = { 100, 200 }
print(s2.issubset(s1)) # True s2 是 s1 的子集
print(s3.issubset(s1)) # False

# 集合关系：超集
print(s1.issuperset(s2)) # True
print(s1.issuperset(s3)) # False

# 集合关系：是否没有交集
print(s2.isdisjoint(s3))
print(s2.isdisjoint(s4)) # True