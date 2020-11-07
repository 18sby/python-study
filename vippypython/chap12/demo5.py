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

# 类属性的使用
# print(Student.native_place)
stu1 = Student('张三', 20)
stu2 = Student('李四', 30)
print(stu1.native_place)
print(stu2.native_place)
Student.native_place = '天津'
print(stu1.native_place)
print(stu2.native_place)

print('\n---类方法的使用---\n')
Student.cm()

print('\n---静态方法的使用---\n')
Student.method()