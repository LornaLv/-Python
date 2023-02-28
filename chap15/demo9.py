# Date: 2023/2/21 下午8:17

file = open('c.txt', 'r')
file.seek(2)
print(file.read())
print(file.tell())
# print(file.read(10))
# print(file.readline())
# print(file.readlines())
file.close()
