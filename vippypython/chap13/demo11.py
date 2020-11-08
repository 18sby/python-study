# 类的赋值与浅拷贝

class CPU:
  pass

class Disk:
  pass

class Computer:
  def __init__(self, cpu, disk):
    self.cpu = cpu
    self.disk = disk

cpu1 = CPU()
cpu2 = cpu1
print(cpu1, id(cpu1))
print(cpu2, id(cpu2))

print('\n------\n')

# 类的浅拷贝
disk = Disk()
computer = Computer(cpu1, disk)

# 浅拷贝，只拷贝一层，后代属性还是用的一样的内存地址
import copy
computer2 = copy.copy(computer)
print(computer, computer.cpu, computer.disk)
print(computer2, computer2.cpu, computer2.disk)

print('\n---深拷贝---\n')

computer3 = copy.deepcopy(computer)
print(computer, computer.cpu, computer.disk)
print(computer3, computer3.cpu, computer3.disk)