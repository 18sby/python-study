# try..except..else..finally

'''
    try
    /  \
except else
  \     /
  finally
'''

try:
  a = int(input('输入第一个整数'))
  b = int(input('输入第二个整数'))
  result = a / b
except BaseException as e:
  print('出错了', e)
else:
  print('计算结果为: ', result)
finally:
  print('程序执行结束，可以选择回收内存')