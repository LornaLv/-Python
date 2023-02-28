# Date: 2023/2/19 下午4:00
# 字符串的替换
s = 'hello,python'
print(s.replace('python', 'java'))

s1 = 'hello,python,python,python'
print(s1.replace('python', 'java', 2))

lst = ['hello', 'world', 'python', 'java']
print(lst, type(lst))
print('|'.join(lst))
print(''.join(lst))

t = ('hello', 'java', 'python')
print(''.join(t))

print('*'.join('Python'))
