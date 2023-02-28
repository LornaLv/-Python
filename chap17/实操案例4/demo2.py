# Date: 2023/2/23 下午3:19
# 任务2：模拟QQ账号登录

id = input('请输入用户名：')
pwd = input('请输入密码：')

if id == '123456789' and pwd == '123':
    print('登录成功')
else:
    print('用户账号不存在，或密码错误')
