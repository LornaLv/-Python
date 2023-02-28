# Date: 2023/2/23 下午3:23
# 任务三：商品价格大竞猜
import random

print('今日竞猜商品为小米扫地机器人，价格在[1000-1500之间]')
price = random.randint(1000,1500)

while True:
    a = float(input('请输入竞猜价格：'))
    if a == price:
        print('猜对了')
        break
    while a >= 0 and a != price:
        if 1000 <= a < price:
            print('小了')
            break
        elif price < a <= 1500:
            print('大了')
            break
        else:
            print('请在合理范围内猜测价格！')
            break
