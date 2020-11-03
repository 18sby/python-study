# 异常处理机制

try:
  a = int(input('输入第一个整数'))
  b = int(input('输入第二个整数'))
  result = a / b
  print('结果为: ', result)
except ZeroDivisionError:
  print('除数不能为0')
except ValueError:
  print('只能输入数字')

print('程序结束')