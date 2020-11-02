# 函数的创建

def add(a, b): # a,b: 形式参数，形参
  c = a + b
  return c

sum = add(1,2) # 1,2: 实际参数，实参
print(sum)

res = add(b = 10, a = 20) # =左侧的变量的名称为 关键字参数
print(res)