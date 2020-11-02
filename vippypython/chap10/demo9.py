# 变量的作用域 全局 - 局部

def fun(a, b):
  c = a + b # c: 局部变量，在函数体内部定义
  return c

sum = fun(10, 20)
print(sum)

name = '鱼沙' # 全局变量
print(name)

def fun2():
  print(name)

fun2()

def fun3():
  global age # 局部变量使用 global 声明，就变成了全局变量
  age = 20
  print(age)

fun3()
print(age)