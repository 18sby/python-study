'''
  从键盘录入密码，最多了录入三次，正确则结束循环
'''
a = 0
while a < 3:
  pwd = input('请输入密码')
  if pwd == '8888':
    print('密码正确')
    break
  else:
    print('密码不正确')
  a += 1