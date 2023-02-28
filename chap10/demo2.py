# Date: 2023/2/19 下午9:01
def fun(arg1, arg2):
    print('arg1:', arg1)
    print('arg2:', arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1:', arg1)
    print('arg2:', arg2)


a1 = 11
a2 = [22, 33, 44]
print('a1:', a1)
print('a2:', a2)
fun(a1, a2)  # 位置传参，arg1,arg2是函数定义处的形参，a1、a2是函数调用处的实参，总结：实参名称与形参名称可以不一致
print('a1:', a1)
print('a2:', a2)

'''在函数的调用过程中，进行参数的传递
如果是不可变对象，在函数体的修改下不会影响实参的值
如果是可变对象，在函数体内的修改会影响到实参的值 arg2得修改，append(10)，会影响a2到值'''
