# Date: 2023/2/19 下午10:34
def fun(a, b=10):
    print('a', a)  # b是在函数的定义处，所以b说形参，而且进行了赋值，所以b称为默认值形参
    print('b', b)


def fun2(*args):  # 个数可变的位置形参
    print(args)


def fun3(**args):  # 个数可变的关键字形参
    print(args)


fun2(1, 2, 3, 4)
fun3(a=11, b=2, c=9, d=0, e=90)


def fun4(a, b, *, c, d):  # 从*之后的参数，在函数调用时，只能采用关键字参数传递
    print('a', a)
    print('b', b)
    print('c', c)
    print('d', d)


# 调用fun4函数
fun4(10, 20, 30, 40)  # 位置实参传递
fun4(a=10, c=20, b=90, d=90)  # 关键字实参传递
fun4(10, 20, d=90, c=20)  # a b采用位置实参传递，c d采用关键字实参传递

'''函数定义时代形参的顺序问题'''


def fun5(a, b, *, c, d, **args):
    pass


def fun6(*args, **arg):
    pass


def fun7(a, b=10, *arg, **args):
    pass
