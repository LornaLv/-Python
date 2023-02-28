# Date: 2023/2/21 下午8:24
file = open('c.txt', 'a')
file.write('hello')
lst = ['java', 'Python', 'world']
file.writelines(lst)
file.close()
