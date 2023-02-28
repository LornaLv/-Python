# Date: 2023/2/24 上午11:43
# 任务二：格式化输出商品的名称和单价
def show(lst):
    for item in lst:
        for i in item:
            print(i, end='\t\t')
        print()


lst = [['01', '电风扇', '美的', 500],
       ['02', '洗衣机', 'TCL', 1000],
       ['03', '微波炉', '老板', 400]]

print('编号\t\t名称\t\t\t品牌\t\t单价')
show(lst)

print('--------------字符串的格式化操作--------------')
print('  编号\t\t 名称\t\t品牌\t\t单价')
for item in lst:
    item[0] = '0000' + item[0]
    item[3] = '￥{:.2f}'.format(item[3])
show(lst)
