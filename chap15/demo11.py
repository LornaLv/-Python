# Date: 2023/2/21 下午8:31

file = open('d.txt', 'a')
file.write('hello')
file.close()
file.write('world')
file.flush()
