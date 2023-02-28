# Date: 2023/2/24 下午3:11
# 任务二：定义学生类录入5个学生信息存储到列表中
class Student(object):
    def __init__(self, name, age, gender, score):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def show(self):
        print(self.name, self.age, self.gender, self.score)


if __name__ == '__main__':
    print('请输入5位学员的信息：（姓名#年龄#性别#成绩）')
    lst = []
    for i in range(1, 6):
        s = input(f'请输入第{i}位学员的成绩：')
        s_lst = s.split('#')
        # 创建学生对象
        stu = Student(s_lst[0], int(s_lst[1]), s_lst[2], float(s_lst[3]))
        lst.append(stu)
    # 遍历列表
    for item in lst:
        item.show()
