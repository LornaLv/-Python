# Date: 2023/2/20 上午10:41
age = input('请输入你的年龄：')
print(type(age))
if int(age) >= 18:
    print('成年人....')

i = 0
while i < 10:
    print(i)
    i += 1

for i in range(3):
    uname = input('请输入用户名：')
    pwd = input('请输入密码：')
    if uname == 'admin' and pwd == 'admin':
        print('登录成功！')
        break
    else:
        print('密码错误')
else:
    print('对不起，三次均输入错误')
