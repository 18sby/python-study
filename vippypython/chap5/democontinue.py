# 输出 1 - 50 之间所有 5 的倍数

for num in range(1, 51):
  if num % 5 != 0:
    continue
  print(num)