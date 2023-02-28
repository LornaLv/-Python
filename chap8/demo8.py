# Date: 2023/2/17 下午7:18
# 集合的数学操作
print('------------交集intersection/&-------------')
s1 = {1, 2, 3, 4}
s2 = {2, 3, 4, 5, 6}
print(s1.intersection(s2))

print('------------并集union/|-------------')
print(s1.union(s2))

print('------------差集difference/减号-------------')
print(s1.difference(s2))

print('------------对称差集symmetric_difference-------------')
print(s1.symmetric_difference(s2))