# Date: 2023/2/20 下午4:36
class Student:  # Student为类名，类名可以由一个或多个单词组成，每个单词的首字母大写，其余小写
    native_place = '山东'  # 直接写在类里的变量称为类属性

    # 初始化方法
    def __init__(self, name, age):
        self.name = name  # self.name称为实例属性，进行了一个赋值操作，将局部变量name的值赋给实例属性
        self.age = age

    # 实例方法
    def eat(self):
        print('学生在吃饭')

    # 静态方法
    @staticmethod
    def method():
        print('我使用staticmethod进行修饰，所以我是静态方法。')

    # 类方法
    @classmethod
    def cm(cls):
        print('我是类方法，因为我使用了classmethod进行修饰')


# 在类之外定义的称为函数，在类之内定义的称为方法
def drink():
    print('喝水')


# 类属性的使用方式
print(Student.native_place)
stu1 = Student('张三', 20)
stu2 = Student('李四', 19)
print(stu1.native_place)
print(stu2.native_place)
Student.native_place = '天津'
print(stu1.native_place)
print(stu2.native_place)

print('-----------类方法的使用方式----------')
# 类方法的使用方式
Student.cm()

print('-----------静态方法的使用方式----------')
# 静态方法的使用方式
Student.method()
