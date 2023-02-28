# Date: 2023/2/16 上午10:37
money = 1000  # 余额
s = int(input('请输入取款金额：'))  # 取款金额
# 判断余额是否充足
if s <= money:
    money = money - s
    print('取款成功，您当前的余额为：', money)
else:
    print('余额不足')
