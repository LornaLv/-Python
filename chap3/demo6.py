# Date: 2023/2/15 下午8:52
# 布尔运算符
a, b = 1, 2
print('------------and--------------')
print(a == 1 and b == 2)  # True and True ---> True
print(a == 1 and b < 2)  # False and False ---> False
print(a < 1 and b == 2)  # False and True ---> False
print(a < 1 and b < 2)  # False and False ---> False

print('------------or--------------')
print(a == 1 or b == 2)  # True and True ---> True
print(a == 1 or b < 2)  # False and False ---> True
print(a < 1 or b == 2)  # False and True ---> True
print(a < 1 or b < 2)  # False and False ---> False

print('------------not 对bool类型的操作进行取反--------------')
f1 = True
f2 = False
print(not f1)

print('------------in 与 not in--------------')
s = 'helloworld'
print('w' in s)
print('k' in s)
print('w' not in s)
print('k' not in s)
