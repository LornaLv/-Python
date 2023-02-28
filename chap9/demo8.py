# Date: 2023/2/19 下午4:14
# 字符串的比较操作
print('apple' > 'app')
print('apple' > 'banana')
print(ord('a'), ord('b'))
print(chr(97), chr(98))

'''
==与is的区别
==比较的是value
is比较的是id是否相等
'''

a = b = 'Python'
c = 'Python'
print(a == b)
print(b == c)
print(a is b)
print(a is c)

print(id(a))
print(id(b))
print(id(c))
