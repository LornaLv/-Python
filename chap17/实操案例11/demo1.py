# Date: 2023/2/24 下午2:13
# 任务一：编写程序输入学员成绩

try:
    score = int(input('请输入分数：'))
    if 0 <= score <= 100:
        print('您的分数为：', score)
    else:
        raise Exception('分数不正确')
except Exception as e:
    print(e)
