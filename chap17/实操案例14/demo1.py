# Date: 2023/2/24 下午4:25
# 任务一：模拟高铁售票系统

import prettytable as pt


# 显示座席
def show_ticket(row_num):
    tb = pt.PrettyTable()
    tb.field_names = ['行 号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(row_num):
        lst = [f'第{i + 1}行' + '', '有票', '有票 ', '有票 ', '有票 ', '有票']
        tb.add_row(lst)
    print(tb)


# 订票
def order_ticket(row_num, row, column):
    tb = pt.PrettyTable()
    tb.field_names = ['行 号', '座位1', '座位2', '座位3', '座位4', '座位5']
    for i in range(row_num):
        if int(row) == i + 1:
            lst = [f'第{i + 1}行' + '', '有票', '有票 ', '有票 ', '有票 ', '有票']
            lst[int(column)] = '已售'
            tb.add_row(lst)
        else:
            lst = [f'第{i + 1}行' + '', '有票', '有票 ', '有票 ', '有票 ', '有票']
            tb.add_row(lst)
    print(tb)


if __name__ == '__main__':
    row_num = 13
    show_ticket(row_num)
'''
    while True:
        choose_num = input('请输入要选择的座位号，如13,5表示13排5号座位:')
        try:
            row, column = choose_num.split(',')
            order_ticket(row_num, row, column)
            choose=input('您要继续购票吗？y/n')
            if choose=='y':
                continue
            elif choose=='n':
                break
            else:
                print('选择错误')
        except:
            print('输入格式有误，如13排5号座位应该输入13,5')
'''


choose_num = input('请输入要选择的座位号，如13,5表示13排5号座位:')
try:
    row, column = choose_num.split(',')
    order_ticket(row_num, row, column)
except:
    print('输入格式有误，如13排5号座位应该输入13,5')


'''
print('+--------+--------+--------+--------+--------+--------+')
print('|  行号  |  座位1  |  座位2  |  座位3  |  座位4  |  座位5  |')
print('+--------+--------+--------+--------+--------+--------+')
for i in range(13):
    for j in range(1):
        print([f'第{i + 1}行', '有 票', '有 票 ', '有 票 ', '有 票 ', '有 票'])
        # tb.add_row(lst)
        #     print(f'| 第{i + 1}行\t|')

print('+--------+--------+--------+--------+--------+--------+')
'''
