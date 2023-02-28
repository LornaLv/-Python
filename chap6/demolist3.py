# Date: 2023/2/16 下午9:29

lst = [10, 20, 30, 40, 50, 60, 70, 80]
print(lst)
print('原列表id：', id(lst))

print('-------------step步长为负数的情况--------------')
# start=1,stop=6,step=1
lst1 = print(lst[1:6:1])
print('切片id：', id(lst1))

# 默认步长为1
lst2 = print(lst[1:6])
lst3 = print(lst[1:6:])

# 步长设置为2
lst4 = print(lst[1:6:2])

# stop=6,step=2,start采用默认
print(lst[:6:2])

# start=1,step=2,stop采用默认
print(lst[1::2])

print('-------------step步长为负数的情况--------------')
# start采用默认，stop采用默认，步长为-1
print(lst[::-1])
# start=7,stop省略，step=-1
print(lst[7::-1])
# start=6,stop=0,step=-2
print(lst[6:0:-2])
