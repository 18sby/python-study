# 继承

class Person(object): # Person 默认也是继承 object 类
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def info(self):
    print(self.name, self.age)

class Student(Person):
  def __init__(self, name, age, stu_no):
    super().__init__(name, age)
    self.stu_no = stu_no

class Teacher(Person):
  def __init__(self, name, age, teach_year):
    super().__init__(name, age)
    self.teach_year = teach_year

stu = Student('鱼沙', 19, 10001)
teacher = Teacher('鲨鱼', 30, 5)

stu.info()
teacher.info()