# Date: 2023/2/24 上午11:07
# 任务三：模拟手机通讯录
lst = []

for i in range(1, 6):
    friend = input(f'请输入第{i}个朋友的姓名与手机号：')
    lst.append(friend)

for item in lst:
    print(item)
