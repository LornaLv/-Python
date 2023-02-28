# Date: 2023/2/16 下午7:09
'''要求输出1-50之间所有5的倍数，5,10,15,20...
5的倍数的共同点：和5的余数为0的数都是5的倍数
使用continue实现
'''
for item in range(1, 51):
    if item % 5 == 0:
        print(item)

print('----------continue-----------')
for item in range(1, 51):
    if item % 5 != 0:
        continue
    print(item)
