# Date: 2023/2/19 下午8:06
# 字符串的切片操作
s = 'hello,Python'
s1 = s[:5]  # 由于没有指定起始位置，所以从0开始
print(s1)  # 由于没有指定结束位置，所以会切到字符串的最后一个元素
s2 = s[6:]
print(s2)
s3 = '!'

newstr = s1 + s3 + s2
print(newstr)

print('-------------------------')
print(id(s))
print(id(s1))
print(id(s2))
print(id(s3))
print(id(newstr))

print('---------切片[start:end:step]---------')
print(s[1:5:1])  # 从1 开始截到5（不包括5），步长为1
print(s[::2])  # 默认从0开始，没有写结束，默认到字符串的最后一个元素，步长为2
print(s[::-1])  # 默认从字符串的最后一个元素开始，到字符串的第一个元素结束，因为步长为负数
print(s[-6::1])
