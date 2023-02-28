# Date: 2023/2/22 上午11:43
# 学生管理系统
import os

filename = 'student.txt'


def main():
    while True:
        menu()
        choic = int(input('请选择：'))
        if choic in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choic == 0:
                answer = input('您确定要退出系统吗？y/n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用，您已退出系统！')
                    break
                else:
                    continue

            elif choic == 1:
                insert()  # 录入学生信息
            elif choic == 2:
                search()  # 查询学生信息
            elif choic == 3:
                delete()  # 删除学生信息
            elif choic == 4:
                modify()  # 修改学生信息
            elif choic == 5:
                sort()  # 对学生信息排序
            elif choic == 6:
                total()  # 统计学生总人数
            elif choic == 7:
                show()  # 显示学生信息


def menu():
    print('====================学生信息管理系统====================')
    print('-----------------------功能菜单-----------------------')
    print('                    1.录入学生信息                     ')
    print('                    2.查找学生信息                     ')
    print('                    3.删除学生信息                     ')
    print('                    4.修改学生信息                     ')
    print('                    5.排序                           ')
    print('                    6.统计学生人数                    ')
    print('                    7.显示所有学生信息                 ')
    print('                    0.退出系统                        ')
    print('-----------------------------------------------------')


def insert():
    student_lst = []
    while True:
        id = input('请输入ID（如1001）：')
        if not id:
            break
        name = input('请输入姓名：')
        if not name:
            break
        try:
            English = int(input('请输入英语成绩：'))
            Python = int(input('请输入Python成绩：'))
            Java = int(input('请输入Java成绩：'))
        except:
            print('输入无效，不是整数类型，请重新输入')
            continue
        # 将录入的学生信息保存到字典当中
        student = {'id': id, 'name': name, 'English': English, 'Python': Python, 'Java': Java}
        # 将学生信息添加到学生列表中
        student_lst.append(student)
        answer = input('是否继续添加？y/n\n')
        if answer == 'n' or answer == 'N':
            break
        elif answer == 'y' or answer == 'Y':
            continue

    # 调用save()函数
    save(student_lst)
    print('学生信息录入完毕！！！')


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    student_query = []
    while True:
        id = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按ID查找请输入1,按姓名查找请输入2：')
            if mode == '1':
                id = input('请输入学生id：')
            elif mode == '2':
                name = input('请输入学生姓名')
            else:
                print('您的输入有误，请重新输入')
                search()
            with open(filename, 'r', encoding='utf-8') as rfile:
                student = rfile.readlines()
                for item in student:
                    d = dict(eval(item))
                    if id != '':
                        if d['id'] == id:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
            # 显示查询结果
            show_student(student_query)
            # 清空列表
            student_query.clear()
            answer = input('是否继续查询？y/n\n')
            if answer == 'y':
                continue
            else:
                break
        else:
            print('暂未保存学生信息')
            return


def show_student(lst):
    if len(lst) == 0:
        print('没有查询到学生信息，无数据显示！')
        return
    # 定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}}'
    print(format_title.format('ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
    # 定义内容的显示格式
    format_data = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('English'),
                                 item.get('Python'),
                                 item.get('Java'),
                                 int(item.get('English')) + int(item.get('Python')) + int(item.get('Java'))))


def delete():
    while True:
        student_id = input('请输入要删除的学生的ID：')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False  # 标记是否删除
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  # 将字符串转成字典
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生信息已被删除')
                    else:
                        print(f'没有找到id为{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show()  # 删除之后，重新显示所有学生信息
            answer = input('是否继续删除？y/n\n')
            if answer == 'y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input('请输入要修改的学员ID：')
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('找到学生信息，可以修改他的信息了！')
                while True:
                    try:
                        d['name'] = input('请输入姓名：')
                        d['English'] = int(input('请输入英语成绩：'))
                        d['Python'] = int(input('请输入Python成绩：'))
                        d['Java'] = int(input('请输入Java成绩：'))
                        break
                    except:
                        print('您的输入有误，请重新输入')
                wfile.write(str(d) + '\n')
                print('修改成功')
            else:
                wfile.write(str(d) + '\n')
        answer = input('是否要继续修改其他学生的信息呢？y/n\n')
        if answer == 'y':
            modify()
        else:
            pass


def sort():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_list=rfile.readlines()
        student_new=[]
        for item in student_list:
            d=dict(eval(item))
            student_new.append(d)
    else:
        return
    asc_or_desc=input('请选择（0,升序 1,降序）：')
    if asc_or_desc=='0':
        asc_or_desc_bool=False
    elif asc_or_desc=='1':
        asc_or_desc_bool=True
    else:
        print('您的输入有误，请重新输入：')
        sort()
    mode=input('请选择排序方式（1，按英语成绩排序 2,按Python成绩排序 3,按Java程序排序 0,按总成绩排序）')
    if mode=='1':
        # student_new.sort(key=lambda,reverse=asc_or_desc_bool)
        pass
    elif mode=='2':
        pass
    elif mode=='3':
        pass
    elif mode=='0':
        pass
    else:
        print('您的输入有误，请重新输入')
        sort()
    show_student(student_new)



def total():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            if students:
                print(f'一共有{len(students)}名学生')
            else:
                print('还没有录入学生信息')
    else:
        print('暂未保存数据信息')


def show():
    student_lst = []
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
            for item in students:
                student_lst.append(eval(item))
            if student_lst:
                show_student(student_lst)
    else:
        print('暂未保存过数据')


if __name__ == '__main__':
    main()
