# 条件语句

money = 1000
s = int(input('请输入取款金额'))
if s > money:
  print('余额不足')
else:
  money -= s
  print('取款成功，还剩', money, '元')