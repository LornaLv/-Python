# Date: 2023/2/16 下午7:49
'''输出一个三行四列的矩形'''
for i in range(1, 4):  # 行数，执行三次，一次是一行
    for j in range(1, 5):
        print('*', end='\t')  # 不换行输出
    print()  # 换行

print('--------九九乘法表--------')
for i in range(1, 10):
    for j in range(1, 10):
        if i >= j:
            print(i, '*', j, '=', i * j, end='\t')
    print()
