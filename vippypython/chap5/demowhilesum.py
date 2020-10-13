# 计算 1 - 100 之间的偶数和

i = 1
sum = 0
while i <= 100:
  if not bool(i % 2):
    sum += i
  i += 1
print('1-100的偶数和: ', sum)