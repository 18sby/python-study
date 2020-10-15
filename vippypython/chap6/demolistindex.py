# list.index(item, start, stop) 返回列表元素 item 的第一个索引，不存在会报错

lst = ['hello', 'world', 100, 'world']
print(lst.index('world'))
# print(lst.index('python'))
print(lst.index('world',2,4))