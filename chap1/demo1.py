# Date: 2023/2/14 下午9:12
# 输出函数print

# 可以输出数字
print(520)
print(2.5)

# 可以输出字符
print('helloworld')
print("hello")

# 可以输出含有运算符的表达式
print(3+1+5)

# 将数据输出到文件中  注意：使用file=...的形式
fp = open('/output/text.txt', 'a+')  # a+：如果文件不存在就创建，存在就在文件内容后创建
print('helloworld', file=fp)
fp.close()

# 不进行换行输出(输出内容在一行当中)
print('hello', 'world', 'Python')