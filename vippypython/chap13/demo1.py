class Car:
  def __init__(self, brand):
    self.brand = brand
  def start(self):
    print('汽车已启动')

car = Car('凯迪拉克XTS')
car.start()
print(car.brand)