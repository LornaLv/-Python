# Date: 2023/2/16 下午7:43
a = 0
while a < 3:
    pwd = input('请输入密码')
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
    a += 1
else:
    print('对不起，三次密码输入均错误')
