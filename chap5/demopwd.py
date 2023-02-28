# Date: 2023/2/16 下午6:52
'''从键盘录入密码，最多录入三次，若正确，则结束循环'''
for _ in range(3):
    pwd = input('请输入密码：')
    if pwd == '8888':
        print('密码正确！')
        break
    else:
        print('密码不正确')
