# Date: 2023/2/16 下午2:55
# 嵌套if语句
'''
会员：购物金额 >=200 8折
            >=100 9折
非会员：购物金额 >=200 9.5折
              不打折
'''
answer = input('您是会员吗？y/n')
money = float(input('请输入购物金额：'))
# 外层判断是否是会员
if answer == 'y':
    if money >= 200:
        print('打8折，付款金额为：', 0.8 * money)
    elif 100 <= money:
        print('打9折，付款金额为：', 0.9 * money)
    else:
        print('不打折，付款金额为：', money)
else:
    print('非会员')
    if money >= 200:
        print('打95折，付款金额为：', 0.95 * money)
    else:
        print('不打折，付款金额为：', money)
