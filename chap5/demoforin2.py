# Date: 2023/2/16 下午5:17
'''
输出100-999之间的水仙花数
举例：153=3*3*3+5*5*5+1*1*1
'''
for item in range(100, 1000):
    ge = item % 10  # 个位上的数
    shi = item // 10 % 10  # 十位
    bai = item // 100  # 百位
    # print(ge, shi, bai)
    # 判断
    if ge**3+shi**3+bai**3==item:
        print(item)
