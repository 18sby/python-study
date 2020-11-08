# 方法重写

class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def info(self):
    print(self.name, self.age)
  def eat(self):
    print('饿了想吃饭')

class Student(Person):
  def __init__(self, name, age, stu_no):
    super().__init__(name, age)
    self.stu_no = stu_no
  def info(self):
    super().info()
    print(self.stu_no)

stu = Student('鱼沙', 19, 10001)
stu.info()