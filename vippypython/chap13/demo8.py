# 特殊属性

# print(dir(object))

class A:
  pass

class B:
  pass

class C(A, B):
  def __init__(self, name, age):
    self.name = name
    self.age = age

class D(A):
  pass

# 创建 C 类的对象
x = C('Jack', 20)

# 实例对象的属性字典
print(x.__dict__)

print(C.__dict__)

print(x.__class__) # 对象所属的类
print(C.__bases__) # C类的父类们的元组
print(C.__base__) # C类继承的第一个父类
print(C.__mro__) # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
print(A.__subclasses__()) # 子类的列表 [<class '__main__.C'>, <class '__main__.D'>]