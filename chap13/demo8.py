# Date: 2023/2/20 下午10:13
print(dir(object))


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


# 创建C类的对象
x = C('Jack', 20)  # x是C类型的实例对象
print(x.__dict__)  # 实例对象的属性字典
print(C.__dict__)
print('--------------------------')
print(x.__class__)  # 输出对象所属于的类
print(C.__bases__)  # 输出C类的父类的元组
print(C.__base__)  # 输出的是C类继承的第一个父类
print(C.__mro__)  # 查看的是类的层次结构
print(A.__subclasses__())
