# 集合的数学操作

s1 = { 10, 20, 30, 40 }
s2 = { 20, 30, 40, 50, 60 }

# 交集操作 intersection = &，不更改原集合
print(s1.intersection(s2))
print(s1 & s2)

# 并集操作 union = | ，不更改原集合
print(s1.union(s2))
print(s1 | s2)

# 差集操作 s1.difference(s2)  在 s1 中除去 s1 和 s2 的并集
print(s1.difference(s2))
print(s1 - s2)
print(s2.difference(s1))
print(s2 - s1)

# 对称差集 两个集合的并集 - 两个集合的交集
print(s1.symmetric_difference(s2))
print(s1 ^ s2)