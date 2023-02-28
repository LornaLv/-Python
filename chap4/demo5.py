# Date: 2023/2/16 上午10:58
# 多分支结构,多选一执行
'''
从键盘录入一个整数：成绩
90-100 A
80-89 B
70-79 C
60-69 D
0-59 E
小于0,大于100为非法数据（不是成绩的有效范围）
'''
score = int(input('请输入一个成绩：'))
# 判断
if score >= 90 and score <= 100:  #90<=score<=100，可简写
    print('你的成绩是A')
elif score >= 80 and score < 90:
    print('你的成绩是B')
elif score >= 70 and score < 80:
    print('你的成绩是C')
elif score >= 60 and score < 70:
    print('你的成绩是D')
elif score >= 0 and score < 60:
    print('你的成绩不及格')
else:
    print('对不起，成绩有误，不在成绩有效范围内')
