# 多态 不同的子类重写父类的方法

class Animal(object):
  def eat(self):
    print('动物会吃东西')

class Dog(Animal):
  def eat(self):
    print('狗吃骨头')

class Cat(Animal):
  def eat(self):
    print('猫吃鱼')

class Person:
  def eat(self):
    print('人吃五谷杂粮')

def fun(obj):
  obj.eat()

fun(Cat())
fun(Dog())
fun(Animal())