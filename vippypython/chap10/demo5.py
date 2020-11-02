# 函数参数的默认值

def fun(a, b = 10):
  print(a, b)

fun(5) # 5 10
fun(20, 30) # 20 30

print('hello', end='\t')
print('python')