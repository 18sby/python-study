# for 循环

for item in 'Python3':
  print(item)

for item in range(1,10,2):
  print(item)

# 如果再循环中不需要自定义变量，可以写 '_'
for _ in range(5):
  print('python3 - ', _)

# for 循环计算 1 - 100 的偶数
sum = 0
for item in range(2,101,2):
  sum += item
print('1 - 100 的偶数和: ', sum)