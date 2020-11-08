# 特殊方法

a = 20
b = 100
c = a + b # 两个整数类型的相加操作

d = a.__add__(b)

print(c)
print(d)

class Student:
  def __init__(self, name):
    self.name = name
  def __add__(self, other):
    return self.name + other.name
  def __len__(self):
    return len(self.name)

stu1 = Student('张三')
stu2 = Student('李四')

print(stu1 + stu2) # 重写 __add__ 函数，让类支持相加方法

s = stu1.__add__(stu2)
print(s)

print('\n------\n')

lst = [11, 22, 33, 44]
print(len(lst))
print(lst.__len__())
print(len(stu1))