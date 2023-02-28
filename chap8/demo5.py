# Date: 2023/2/17 下午6:17
# 集合的创建方式
print('-------------第一种创建方式：使用{}--------------')
s = {2, 2, 3, 4, 5, 6, 5, 7, 7}  # 集合中的元素不允许重复
print(s)

print('-------------第二种创建方式：使用内置函数set()--------------')
s1 = set(range(6))
print(s1, type(s1))
s2 = set([1, 2, 3, 4, 4, 5, 6])
print(s2, type(s2))
s3 = set((1, 2, 3, 4, 3, 2, 3, 4, 5, 6, 4))
print(s3, type(s3))
s4 = set('Python')
print(s4, type(s4))

# 定义一个空集合
s5 = set()
print(s5, type(s5))
