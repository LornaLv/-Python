# Date: 2023/2/21 上午9:49
class CPU:
    pass


class Disk:
    pass


class Computer:
    def __init__(self, cpu, disk):
        self.cpu = cpu
        self.disk = disk


# (1)变量的赋值
cpu1 = CPU()
cpu2 = cpu1
print(cpu1, id(cpu1))
print(cpu2, id(cpu2))

disk = Disk()  # 创建一个硬盘类的对象
print(disk, id(disk))
computer = Computer(cpu1, disk)  # 创建一个计算机类的对象

import copy

# (2)类的浅拷贝
print('----------浅拷贝----------')
computer2 = copy.copy(computer)
print(computer, computer.cpu, computer.disk)
print(computer2, computer2.cpu, computer2.disk)

# (3)类的深拷贝
print('----------深拷贝----------')
computer3 = copy.deepcopy(computer)
print(computer, computer.cpu, computer.disk)
print(computer3, computer3.cpu, computer3.disk)
