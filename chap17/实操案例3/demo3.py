# Date: 2023/2/23 下午2:44
# 计算能量的消耗
a = int(input('请输入您当天行走的步数：'))
calorie = a * 28
print('您今天一共消耗了卡路里：{0}(即{1}千卡)'.format(calorie, calorie / 1000))
