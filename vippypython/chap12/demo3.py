# 实例的创建

class Student:
  # 类属性
  native_place = '吉林'

  def __init__(self, name, age):
    # self.name 实例属性
    self.name = name
    self.age = age

  # 实例方法
  def eat(self):
    print('学生在吃饭')

  # 静态方法
  @staticmethod
  def method():
    print('我是静态方法，我里面不允许写 self')
  
  # 类方法
  @classmethod
  def cm(cls):
    print('我是类方法')

stu1 = Student('张三', 20)
# print(type(stu1)) # <class '__main__.Student'>
# print(stu1)
stu1.eat() # 实例对象.方法
Student.eat(stu1) # 类.方法(实例对象)
print(stu1.name)
print(stu1.age)