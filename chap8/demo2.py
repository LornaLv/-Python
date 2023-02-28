# Date: 2023/2/17 下午3:52

'''元组的创建方式'''

print('-----------第一种创建方式，使用小括号（）-----------')
t = ('Python', 'world', 90)
print(t)
print(type(t))
t2 = 'Python', 'world', 98  # 省略了小括号
print(t2)
print(type(t2))

print('-----------第二种创建方式，使用内置函数tuple-----------')
t1 = tuple(('Python', 'world', 98))
print(t1)
print(type(t1))

print('-----------第三种创建方式，如果元组中只有一个元素，逗号不能省-----------')
t3 = ('python',)
print(t3)
print(type(t3))
t4 = ('python')
print(t4)
print(type(t4))

print('-----------空元组的创建方式-----------')
# 空元组的创建
t5=()
t6=tuple()
print(t5)
print(t6)

print('-----------空列表、空字典、空元组----------')
lst=[]
lst1=list()
d={}
d1=dict()
t7=()
t8=tuple()
print('空列表：',lst,lst1)
print('空字典：',d,d1)
print('空元组：',t7,t8)


