# Date: 2023/2/23 下午6:21
# 任务二：模拟12306火车票订票下单
d = {'G1569': ['北京南-天津南', '18:05', '18:39', '00:34'],
     'G1567': ['北京南-天津南', '18:15', '18:49', '00:34'],
     'G8917': ['北京南-天津西', '18:25', '19:19', '00:59'],
     'G203': ['北京南-天津南', '18:35', '19:09', '00:34'], }

print(' 车次\t\t出发站-到达站\t\t出发时间\t\t到达时间\t\t历史时长')
for item in d:
    print(item, end='\t\t')
    for i in d[item]:
        print(i, end='\t\t')
    print()  # 换行

while True:
    # 输入要购买的车次
    train_num = input('请输入要购买的车次：')
    if train_num in d:
        break
    else:
        print('不存在该车次，请重新选择')
        continue

persons = input(f'您已选择{train_num}车次，请输入乘车人，如果是多人请使用逗号分割：')
# print(f'您已购买了{train_num}次列车，{d[item]},请{persons}尽快换取纸质车票。【铁路客服】')
s1 = f'您已购买了{train_num}次列车，'
train_info = d[train_num]
s2 = train_info[0]
s3 = train_info[1]
s4 = f'请{persons}尽快换取纸质车票。【铁路客服】'
print(s1 + s2 + ' ' + s3 + ' 开， ' + s4)
