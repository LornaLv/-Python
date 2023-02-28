# Date: 2023/2/23 下午12:08
# 输出你的身体指标
height = 170
weight = 60
bmi = weight / (height + weight)
print('您的身高是：' + str(height))
print('您的体重是：' + str(weight))
print('您的BMI指数是：' + '{:0.2f}'.format(bmi))
