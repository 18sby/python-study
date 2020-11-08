# __new__    __init__

class Person:

  def __new__(cls, *args, **kwargs):
    print('__new__被调用了，cls的id值为{0}'.format(id(cls)))
    obj = super().__new__(cls)
    print('创建的对象的id为{0}'.format(id(obj)))
    return obj

  def __init__(self, name, age):
    print('__init__调用，self的值为:{0}'.format(id(self)))
    self.name = name
    self.age = age

print('object这个类对象的id为{0}'.format(id(object)))
print('Person这个类对象的id为{0}'.format(id(Person)))

# 创建 Person 类的实例对象
p1 = Person('张三', 20)
print('p1这个实例对象的id为{0}'.format(id(p1)))