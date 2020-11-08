# object 类

class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self): # 重写了父类 object 的 __str__ 函数
    return '我的名字是鱼沙'

stu = Student('鱼沙', 19)
print(dir(stu))
print(stu.__str__())
print(type(stu))