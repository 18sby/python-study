# 类的创建

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