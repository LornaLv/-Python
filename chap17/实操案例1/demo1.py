# Date: 2023/2/23 上午10:20
# 实操案例1
# 任务1：向文件输出’奋斗成就更好的你‘
print('--------------任务一--------------')

print('第一种方法：使用print方式进行输出（输出目的地是文件）')
fp = open('/chap17/实操案例1/output1.txt', 'a+')
print('奋斗成就更好的你', file=fp)
fp.close()

print('第二种方法：使用文件读写操作')
with open('/chap17/实操案例1/output2.txt', 'w') as file:
    file.write('奋斗成就更好的你')
