# Date: 2023/2/17 下午4:34
'''元组的遍历'''
t=('python','world',98)
print('-------------第一种获取元组的方式,使用索引-------------')
print(t[0])
print(t[1])
print(t[2])
print('-------------第二种获取元组的方式,遍历元组，for...in -------------')
for item in t:
    print(item)
