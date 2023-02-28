# Date: 2023/2/20 下午8:29
class Person(object):  # Person继承object类
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)


class Student(Person):
    def __init__(self, name, age, stu_num):
        super().__init__(name, age)
        self.stu_num = stu_num
    def info(self):
        super().info()
        print(self.stu_num)


class Teacher(Person):
    def __init__(self, name, age, teachofyear):
        super().__init__(name, age)
        self.teachofyear = teachofyear
    def info(self):
        super().info()
        print(self.teachofyear)


stu = Student('张三', 20, '1001')
stu.info()
print('---------------------')


tea = Teacher('李四', 38, 10)
tea.info()
