# Date: 2023/2/24 下午3:48
# 任务二：请使用面向对象的思想，设计自定义类，描述出租车和家用轿车的信息

class Car(object):
    def __init__(self, cartype, no):
        self.cartype = cartype
        self.no = no

    def start(self):
        pass

    def stop(self):
        pass


class Taxi(Car):
    def __init__(self, cartype, no, company):
        super().__init__(cartype,no)
        self.company = company

    def start(self):
        print('乘客您好')
        print(f'我是{self.company}出租车公司的，我的车牌是{self.no},请问您要去哪里？')

    def stop(self):
        print('目的地到了，请您付款下车，欢迎再次乘坐')


class FamilyCar(Car):
    def __init__(self, cartype, no, name):
        super().__init__(cartype,no)
        self.name = name

    def start(self):
        print(f'我是{self.name},我的汽车我做主')

    def stop(self):
        print('目的地到了，我们去玩吧！')


if __name__ == '__main__':
    car = Car('1', '2')
    car.stop()
    car.start()

    taxi = Taxi('上海大众', '京A9765','长城')
    taxi.start()
    taxi.stop()
    print('-'*30)
    familycar = FamilyCar('广汽丰田', '京B8888', '武大郎')
    familycar.start()
    familycar.stop()
