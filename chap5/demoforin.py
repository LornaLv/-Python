# Date: 2023/2/16 下午5:11
for item in 'Python':  # 第一次取出来的事P，将P赋值给item，将item的值输出
    print(item)

# range（）产生一个整数数列，也是一个可迭代对象
for i in range(10):
    print(i)

# 如果在循环体中不需要使用到自定义变量，可将自定义变量写为下划线
for _ in range(5):
    print('人生苦短，我用python')

# 使用for循环计算1-100之间的偶数累加和
sum = 0
for item in range(1, 101):
    if (item % 2 == 0):
        sum = sum + item
print('1-100之间的偶数累加和为：', sum)
