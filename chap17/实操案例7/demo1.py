# Date: 2023/2/23 下午6:20
# 任务一：根据星座测试性格特点
# 创建星座的列表
constellation = ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座',
                 '水瓶座', '双鱼座']
# 创建性格的列表
nature = ['积极乐观', '固执内心', '圆滑世故', '多愁善感', '迷之自信', '精明计较', '犹豫不决', '阴暗消极', '放荡不羁',
          '务实本分', '作天作地', '安于现状']

# 将两个列表转成集合
d = dict(zip(constellation, nature))
# for item in d:
#     print(item,d[item])

while True:
    key = input('请输入您的星座名称：')
    if key in d:
        print(key, '的性格特点为：', d.get(key))
        break
    else:
        print('对不起，您输入的星座有误')
        continue
