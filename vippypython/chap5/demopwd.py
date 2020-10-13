'''
  从键盘录入密码，最多了录入三次，正确则结束循环
'''
for item in range(3):
  pwd = input('请输入密码')
  if pwd == '8888':
    break
  else:
    print('密码不正确')