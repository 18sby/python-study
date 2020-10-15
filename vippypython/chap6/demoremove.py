# 移除列表中的元素 remove

lst = [10,20,30,40,50,70,30]

# 如果有重复的，从列表中移除第一个元素
lst.remove(30)
print(lst)

# pop 根据索引移除元素
lst.pop(1)
print(lst)

# 指定的索引不存在，将抛出异常
# lst.pop(5)

# 不写参数，会默认删除列表最后的元素
lst.pop()
print(lst)

print('\n---切片操作，取出至少一个元素，将产生一个新的列表对象---\n')
newList = lst[1:3]
print('原列表', lst)
print('新列表', newList)

'''
  不产生新的列表对象，而删除原列表中的内容
'''
lst[1:3] = []
print('原列表', lst)

# clear() 清除列表中的所有元素
lst.clear()
print(lst)

# del 将删除列表对象
del lst
# print(lst) # name 'lst' is not defined