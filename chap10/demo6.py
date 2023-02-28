# Date: 2023/2/19 下午10:06
def fun(*args):
    print(args)  # 函数定义时，可变的位置参数
    # print(args[0])


fun(10)
fun(20, 20)
fun(45, 20, 30)


def fun1(**args):
    print(args)


fun1(a=20)
fun1(a=98, b=20, c=20)

# def fun2(*arg,*a): #可变的位置参数只能是一个
#     pass

# def fun2(**args,**a): #可变的关键字参数只能有一个
#     pass

def fun2(*a,**b):
    pass

# def fun3(**a,*b): #在一个函数的定义过程中，既有个数可变的关键字形参，也有个数可变的位置形参，要求个数可变的位置形参放在个数可变的关键字形参之前
    # pass