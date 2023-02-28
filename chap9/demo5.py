# Date: 2023/2/19 下午3:38
# 字符产的分割
s = 'hello world python'
lst = s.split()
print(lst)

s1 = 'hello|world|python'
lst1 = s1.split(sep='|')
print(lst1)

s2 = 'hello|world|python|1'
lst2 = s2.split(sep='|', maxsplit=2)
print(lst2)

print('----------rsplit:从右侧开始拆分------------')
print(s.rsplit())
print(s1.rsplit(sep='|'))
print(s2.rsplit(sep='|', maxsplit=2))
