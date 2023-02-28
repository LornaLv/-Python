# Date: 2023/2/19 下午3:49
# 字符串的判断
s = 'hello,python'
print('------------isidentifier--------------')
print('1、', s.isidentifier())
print('2、', 'hello'.isidentifier())
print('3、', '张三'.isidentifier())
print('4、', '张三123'.isidentifier())

print('------------isspace--------------')
print('1、', s.isspace())
print('2、', '\t'.isspace())

print('------------isalpha--------------')
print('1、', s.isalpha())
print('2、', 'hello'.isalpha())
print('3、', '张三'.isalpha())
print('4、', '张三123'.isalpha())

print('------------isdecimal--------------')
print('1、', s.isdecimal())
print('2、', 'hello'.isdecimal())
print('3、', '张三'.isdecimal())
print('4、', '123'.isdecimal())

print('------------isnumerc--------------')
print('1、', s.isnumeric())
print('2、', '三'.isnumeric())
print('3、', '12783'.isnumeric())
print('4、', '123四'.isnumeric())

print('------------isalnum--------------')
print('1、', s.isalnum())
print('2、', '三'.isalnum())
print('3、', '12783'.isalnum())
print('4、', '123四3sfch'.isalnum())
