# in, not in 在列表中的应用

print('p' in 'python')
print('k' not in 'python')

lst = [10,20,'python','hello']
print(10 in lst)
print(100 in lst)
print(10 not in lst)

for index, item in enumerate(lst):
  print(index, item)