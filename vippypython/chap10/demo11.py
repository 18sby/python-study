# 斐波那契数列

# 递归
# ll = 1
# l = 1
# def fib(n):
#   if (n == 1 or n == 2):
#     return 1
#   else:
#     return fib(n-1) + fib(n-2)

# res = fib(30)
# print(res)

# 动态规划
def fib(n):
  lst = [1,1]
  if (n == 1 or n == 2):
    return 1
  else:
    for i in range(2, n+1):
      lst.append(lst[i-2] + lst[i-1])
    return lst[-1]

print(fib(3))