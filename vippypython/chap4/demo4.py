# 嵌套条件语句

answer = input('您是会员吗？y/n_')
money = float(input('请输入购物金额_'))
if answer == 'y':
  if money >= 200:
    print('打九折，您的付款金额为', money * 0.9, '元')
  elif money >= 100:
    print('打八折，您的付款金额为', money * 0.8, '元')
  else:
    print('不打折，您的付款金额为', money * 1, '元')
else:
  if money >= 200:
    print('打九五折，您的付款金额为', money * 0.95, '元')
  else:
    print('不打折，您的付款金额为', money * 1, '元')