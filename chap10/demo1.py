# Date: 2023/2/19 下午8:49
# 函数的定义和使用
def calc(a, b):  # a、b称为形式参数（形参），形参出现在函数的定义处
    c = a + b
    return c


result = calc(10, 20)  # 10、20称为实际参数的值（实参），实参出现在函数的调用处
print(result)

result1 = calc(b=10, a=20)  # =左侧的变量的名称称为关键字参数
print(result1)
