# Date: 2023/2/16 下午8:16
'''流程控制语句break、continue在二重循环中的使用'''
for i in range(5):
    for j in range(1, 11):
        if j % 2 == 0:
            # break
            continue
        print(j, end='\t')
    print()
