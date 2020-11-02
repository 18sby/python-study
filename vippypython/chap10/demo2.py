# 函数的参数传递

def fun(arg1, arg2):
  print(arg1, arg2)
  arg1 = 100
  arg2.append(10)
  print(arg1, arg2)

n1 = 11
n2 = [22, 33, 44]
fun(n1, n2)
print(n1, n2)