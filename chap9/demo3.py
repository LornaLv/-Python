# Date: 2023/2/19 下午2:43
# 字符串中的大小写转换的方法
s = 'hello,python'
print(s, id(s))
print('--------------upper:把所有字符都转成大写--------------')  # 转成大写之后会产生新的字符串
print(s.upper(), id(s.upper()))
print(s, id(s))

print('--------------lower:把所有字符都转成小写--------------')
print(s.lower(), id(s.lower()))
print(s, id(s))

print('--------------swapcase:把字符串中所有大写字母转成小写字母，把所有小写字母转成大写字母--------------')
print(s.swapcase(), id(s.swapcase()))
print(s, id(s))

print('--------------capitalize：把第一个字符转换为大写，把其余字符转换为小写--------------')
print(s.capitalize(), id(s.capitalize()))
print(s, id(s))
