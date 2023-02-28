# Date: 2023/2/21 下午8:31

file = open('d.txt', 'a')
file.write('hello')
file.flush()
file.write('world')
file.close()
