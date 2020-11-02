def fun(num):
  odd = []
  even = []
  for i in num:
    if i % 2:
      odd.append(i)
    else:
      even.append(i)
  return odd, even

lst = [10, 29, 34, 23, 44, 53, 55]
print(fun(lst)) # ([29, 23, 53, 55], [10, 34, 44])

'''
  1. 如果函数没有返回值，【函数执行完成之后，可以不写 return，返回值为 None】
  2. 函数的返回值如果是一个，直接返回原类型
  3. 函数的返回值为多个，那么返回的结果为元组
'''

def fun1():
  print('hello')

print(fun1())

def fun2():
  return 'hello'

res = fun2()
print(res)

def fun3():
  return 'hello', 100

t = fun3()
print(t[0], t[1])