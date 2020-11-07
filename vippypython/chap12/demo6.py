# 给类实例动态绑定属性和方法

class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def eat(self):
    print(self.name + '在吃饭')

stu1 = Student('张三', 20)
stu2 = Student('李四', 30)

print(id(stu1))
print(id(stu2))

stu2.gender = '女'
print(stu1.name, stu1.age)
print(stu2.name, stu2.age, stu2.gender)

print('\n------\n')
stu1.eat()
stu2.eat()

def show():
  print('stu1 show function')

stu1.show = show

stu1.show()