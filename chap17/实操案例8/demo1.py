# Date: 2023/2/24 上午10:06
# 任务一：我的咖啡你做主
print('-----------方法一---------')
coffee_name = ('蓝山', '卡布奇诺', '拿铁', '皇家咖啡', '女王咖啡', '美丽与哀愁')
print('您好！欢迎光临小喵咖啡屋')
print('本店经营的咖啡有：', end='\t')

for index, item in enumerate(coffee_name):
    print(index + 1, '.', item, end='\t\t')
index = int(input('\n请输入您喜欢的咖啡店编号:'))
if 0 <= index <= len(coffee_name):
    print(f'您的咖啡到了,【{coffee_name[index - 1]}】好了,请您慢用...')

print('----------方法二----------')
print('您好！欢迎光临小喵咖啡屋')
print('本店经营的咖啡有：', end='\t')

d = {1: '蓝山', 2: '卡布奇诺', 3: '拿铁', 4: '皇家咖啡', 5: '女王咖啡', 6: '美丽与哀愁'}
for i in range(1, 7):
    print(f'{i}.' + d.get(i), end='\t')

num = int(input('\n请输入您喜欢的咖啡店编号:'))
if num in d.keys():
    print(f'您的咖啡到了,【{d.get(num)}】好了,请您慢用...')
