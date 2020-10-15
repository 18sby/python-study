# 列表切片 list[start:stop:step] start - stop 左闭右开区间

lst = [10,20,30,40,50,60,70,80]
print('原列表', id(lst))
lst2 = lst[1:6:1]
print('切的片段', id(lst2))

# 默认步长为 1
print(lst[1:6])
print(lst[1:6:2])

# 默认 start 为 0
print(lst[:6:2])

# stop 默认为 lst 的长度
print(lst[1::2])

print('\n步长为负数的情况\n')

# 倒序输出
print(lst[::-1])

# start = 7  stop 省略 step = -1
print(lst[7::-1])

print(lst[6:0:-2])