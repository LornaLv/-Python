# Date: 2023/2/20 下午9:56
class Animal(object):
    def eat(self):
        print('动物要吃东西')


class Dog(Animal):
    def eat(self):
        print('狗吃骨头')


class Cat(Animal):
    def eat(self):
        print('猫吃鱼')


class Person(object):
    def eat(self):
        print('人吃五谷杂粮')


# 定义一个函数
def fun(obj):
    obj.eat()


# 调用fun
fun(Cat())
fun(Dog())
fun(Animal())
fun(Person())
