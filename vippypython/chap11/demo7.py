# try..except..else 
# 如果没有抛出异常执行 else 代码块，如果有异常，执行 except 代码块

try:
  a = int(input('输入第一个整数'))
  b = int(input('输入第二个整数'))
  result = a / b
except BaseException as e:
  print('出错了', e)
else:
  print('计算结果为: ', result)