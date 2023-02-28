# Date: 2023/2/23 下午2:59
# 任务1：支付密码的验证
password = input('请输入支付宝支付密码：')
if password.isdigit():
    print('支付数据合法')
else:
    print('支付数字不合法，支付密码只能是数字！')

print('支付数据合法' if password.isdigit() else '支付数字不合法，支付密码只能是数据')
