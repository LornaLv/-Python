# Date: 2023/2/15 下午4:34
name = '张三'
age = 20

print(name, type(name))
print(age, type(age))

# name与age的数据类型不同
# print('我叫'+name+'今年'+age+'岁')
# 当将str类型与int类型进行连接时，报错；解决方案：类型转换
print('我叫' + name + ',今年' + str(age) + '岁')

print('----------str()将其他类型转换为str类型-----------')
a = 10
b = 2.5
c = False
print(str(a), type(str(a)))
print(str(b), type(str(b)))
print(str(c), type(str(c)))

print('----------int()将其他类型转换为int类型-----------')
a1 = 10
a2 = 9.87
a3 = 9.1
a4 = False
a5 = 'hello'
print(type(a1), type(a2), type(a3), type(a4), type(a5))
print(int(a1), type(int(a1)))
print(int(a2), type(int(a2)))
print(int(a3), type(int(a3)))
print(int(a4), type(int(a4)))
# print(int(a5), type(int(a5)))


print('----------float()将其他类型转换为float类型-----------')
b1 = '128.98'
b2 = '76'
b3 = True
b4 = 'hello'
b5 = 98
print(type(b1), type(b2), type(b3), type(b4), type(b5))
print(float(b1), type(float(b1)))
print(float(b2), type(float(b2)))
print(float(b3), type(float(b3)))
# print(float(b4),type(float(b4)))
print(float(b5), type(float(b5)))
