'''
  除数一个三行四列的矩形
'''

# for i in range(1,4): # 行数
#   for j in (1,5):
#     print('*', end='\t') # 不换行输出
#   print('') # 换行

a = 2
row = ''
for i in range(1,10):
  for j in range(1,a):
    row += ( str(i) + '*' + str(j) + '=' + str(i*j) + ' ' )
  print(row)
  row = ''
  a += 1