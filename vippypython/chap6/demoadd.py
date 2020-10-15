# 向列表的末位添加一个元素 list.append

lst = [10,20,30]
print('添加之前', lst, id(lst))
lst.append(40)
print('添加之后', lst, id(lst))

lst2 = ['hello', 'world']
# 将 lst2 作为一个元素添加到列表的末尾
# lst.append(lst2)
# 将 lst2 遍历后的每一个元素分别添加到 lst 的末尾
lst.extend(lst2)
lst.extend([100,200])
print(lst)

# 在任意位置添加一个元素
lst.insert(1,90)
print(lst)

# 在任意位置添加 n 个元素
lst3 = [True, False, 'hello']
# 从 1 开始，把后面的内容切掉，用一个新的列表 lst3 替换
lst[1:] = lst3
print(lst)