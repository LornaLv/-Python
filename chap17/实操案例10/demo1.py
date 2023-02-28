# Date: 2023/2/24 上午11:55
# 任务一：Mini计算器
def calc(a, b, c):
    while True:
        if c == '+':
            print(a + b)
        elif c == '-':
            print(a - b)
        elif c == '*':
            print(a * b)
        elif c == '/':
            print(a / b)
        else:
            print('输入有误，请重新输入')


a = int(input('请输入第一个整数：'))
b = int(input('请输入第二个整数：'))
c = input('请输入运算符：')
calc(a, b, c)
