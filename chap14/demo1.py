# Date: 2023/2/21 下午2:39
def fun():
    pass


def fun2():
    pass


class Student:
    native_place = '山东'  # 类属性

    def eat(self, name, age):
        self.name = name
        self.age = age

        pass

    @classmethod
    def cm(cls):
        pass

    @staticmethod
    def sm():
        pass


a = 1
b = 2
print(a + b)
