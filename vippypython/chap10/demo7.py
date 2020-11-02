def fun(a, b, c):
  print('a:', a)
  print('b:', b)
  print('c:', c)

fun(10, 20, 30)

lst = [11, 22, 33]
# - *lst 在列表调用时候，将列表解构
fun(*lst)

# 关键字实参，对应赋值
fun(a=100, b=200, c=300)

# - **dic 在函数调用时候，将字典解构
dic = { 'a': 111, 'b': 222, 'c': 333 }
fun(**dic)