class Student:
  def __init__(self, name, age):
    self.name = name
    self.__age = age # 不希望在外部被使用，所以加了两个下划线，但是也有办法在外部使用
  def showAge(self):
    print(self.name + self.__age + '岁')

stu1 = Student('鱼沙', '18')

stu1.showAge()

print(stu1._Student__age) # 在类的外部可以访问实例的 __age 属性