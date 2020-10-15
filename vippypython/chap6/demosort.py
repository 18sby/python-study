lst = [20,40,10,98,54]

print('排序前的列表', lst, id(lst))

# 开始排序 list.sort 默认升序 reverse=False
lst.sort()
print('排序后的列表', lst, id(lst))

# 通过制定关键字参数，将列表中的元素降序排序
lst.sort(reverse=True)
print(lst)

# reverse=False 升序
lst.sort(reverse=False)
print(lst)

print('\n---使用内置函数 sorted 对列表进行排序，将产生一个新的列表对象---\n')

lst = [20,40,10,98,54]
print('排序前的列表', lst, id(lst))

# 升序
newList = sorted(lst, reverse=False)
print('排序后产生的新列表', newList)

# 降序
newList = sorted(lst, reverse=True)
print('排序后产生的新列表', newList)