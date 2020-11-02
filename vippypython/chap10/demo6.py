# 个数可变的位置参数 *args 接受所有参数，为元组，即使是一个参数，也是元组
def fun(*args):
  print(args)

fun(10)
fun(10, 20, 30)

# 个数可变的关键字形参 **args 接收所有参数，为字典
def fun1(**args):
  print(args)

fun1(a='10', b=20)
fun1(a=10, b=20, c=30)


def fun2(*args1, **args2):
  print(args1, args2)

fun2()

# 报错，不能同时使用两个 * 或者两个 **
# def fun3(*args, *er):
#   print(args, er)