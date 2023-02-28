# Date: 2023/2/24 下午2:39
# 定义一个函数圆的类，计算圆的面积和周长
import math


class Circle(object):
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return math.pi * math.pow(self.r, 2)

    def get_Perimeter(self):
        return 2 * math.pi * self.r


if __name__ == '__main__':
    r = int(input('请输入圆的半径：'))
    c = Circle(r)
    print('圆的面积为：', c.get_area())

    print('圆的周长为：', c.get_Perimeter())

    print(f'圆的面积为：{c.get_area():.2f}')

    print(f'圆的周长为：{c.get_Perimeter():.2f}')
