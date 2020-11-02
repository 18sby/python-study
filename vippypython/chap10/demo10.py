# 函数递归

def fac(n):
  if (n == 1):
    return n
  else:
    return n * fac(n-1)

res = fac(6)
print(res)