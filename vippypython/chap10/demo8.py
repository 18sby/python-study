# 默认值形参

def fun(a, b=10):
  print('a:', a)
  print('b:', a)

def fun2(*args): # 个数可变的位置形参 元组
  print('args:', args)

def fun3(**args): # 个数可变的关键字形参 字典
  print('args:', args)

fun2(10, 20, 30, 40)
fun3(a=11, b=22, c=33, d=44)

def fun4(a,b,*,c,d): # 从 * 之后的参数，在函数调用时，只能采用关键字参数传递
  print('a:', a)
  print('b:', b)
  print('c:', c)
  print('d:', d)

# fun4(10,20,30,40)
fun4(a=10, b=20, c=30, d=40)
fun4(10, 20, c=30, d=40)

# 函数定义时的形参的顺序问题
def fun5(a,b,*,c,d,**args):
  pass

def fun6(*args, **args2):
  pass

def fun7(a, b=10, *args, **args2):
  pass
