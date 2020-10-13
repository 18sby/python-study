# 注意：如果三次之内输入正确密码，那么最后的 else 不会走

for item in range(3):
  pwd = input('请输入密码')
  if pwd == '8888':
    print('密码正确')
    break
  else:
    print('密码不正确')
else:
  print('对不起三次均是错误')