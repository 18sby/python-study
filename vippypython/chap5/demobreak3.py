# 流程控制语句 break 与 continue 在二重循环中的使用

for i in range(5):
  for j in range(1,11):
    if j % 2 == 0:
      continue
    print(j,end='\t')
  print()