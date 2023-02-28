# Date: 2023/2/23 下午4:27
# 任务二：模拟用户登录

for i in range(3):
    user = input('请输入用户名：')
    pwd = input('请输入密码：')
    if user == 'admin' and pwd == '8888':
        print('登录成功')
        break
    while user != 'admin' or pwd != '8888':
        if 0 <= i < 2:
            print('用户名或密码不正确')
            print('您还有{0}次机会'.format(2 - i))
            break
        else:
            print('对不起，三次均输入错误，请联系后台管理员')
            break
