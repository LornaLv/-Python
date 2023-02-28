# Date: 2023/2/23 下午5:01
# 猜数游戏
import random

number = random.randint(1, 100)
total = 0

while True:
    num = int(input('我在心中有一个1-100之间的数，请你猜一猜：'))
    if num == number:
        print('恭喜你猜对了')
        total += 1
        break
    while num != number:
        if num < number:
            print('小了')
            total += 1
            break
        elif num > number:
            print('大了')
            total += 1
            break
        else:
            print('猜测数据无效，请在1-100之间进行猜测！')
print(f'您一共猜了{total}次')

print('--------------方法二--------------')
number1=random.randint(1,100)
for i in range(1, 100):
    num1 = int(input('我在心中有一个1-100之间的数，请你猜一猜：'))
    if num1 < number1:
        print('小了')
    elif num1 > number1:
        print('大了')
    else:
        print('恭喜你猜对了')
        break
print(f'您一共猜了{i}次')
