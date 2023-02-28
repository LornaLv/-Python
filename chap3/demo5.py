# Date: 2023/2/15 下午8:40

# 比较运算符
a, b = 10, 20
print('a>b吗?', a > b)  # False
print('a<b吗?', a < b)
print('a<=b吗?', a <= b)
print('a>=b吗?', a >= b)
print('a==b吗?', a == b)
print('a!=b吗?', a != b)

'''
= 称为赋值运算符，== 称为比较运算符
一个变量由三部分组成：标识、类型、值
== 比较的是值
比较对象的标识用 is
'''
print('-------------------------------')
c = 10
d = 10
print(c == d)  # True,说明a与b的walue相等
print(c is d)  # True,说明a与b的id标识相等
print(c is not d)

print('-------------------------------')
list1 = [11, 22, 33, 44]
list2 = [11, 22, 33, 44]
print(list2 == list1)  # value
print(list2 is list1)  # id
print(id(list1))
print(id(list2))
print(list2 is not list1)
