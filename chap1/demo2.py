# Date: 2023/2/15 上午9:41
# 转义字符

print('hello\nworld')  # \ + 转移功能的首字母    n--newline的首字母
print('hello\tworld')  # t--tab 制表符、单位为4、占满才重开一个制表符
print('helloooo\tworld')
print('hello\rworld')  # r-return 光标移动到本行的开头
print('hello\bworld')  # b--backspace 回退一个字符

print('http:\\\\www.baidu.com')
print('老师说：\'大家好\'')

# 原字符：不希望字符串中的转义字符起作用，就使用转义字符，就是在字符串之前加上r或R
print(r'hello\nworld')

# 注意事项：最后一个字符不能是\
print(r'hello\nworld\\')