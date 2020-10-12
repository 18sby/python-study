# 比较运算符

a,b = 10,20
print('a 大于 b 吗？', a > b)
print('a 小于 b 吗？', a < b)
print('a <= b 吗？', a <= b)
print('a >= b 吗？', a >= b)
print('a == b 吗？', a == b)
print('a != b 吗？', a != b)

'''
  =  赋值运算符
  == 比较运算符

  一个变量由三部分组成：标识、类型、值
    == 比较的是什么？
      只比较值
  
  比较对象的标识使用 is
'''

a = 10
b = 10
print(a == b) # True a 与 b 的值相等
print(a is b) # True a 与 b 的标识相等，共用一个标识

# todo 暂时没学的知识点
list1 = [11,22,33,44]
list2 = [11,22,33,44]
print(id(list1), id(list2))
print(list1 == list2) # True
print(list1 is list2) # False
print(a is not b) # False
print(list1 is not list2) # True