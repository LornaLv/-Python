# Date: 2023/2/17 下午6:25
# 集合的相关操作
s = {10, 20, 30, 40, 50, 60, 405}
# 集合元素的判断操作
print('--------集合元素的判断操作---------')
print(10 in s)
print(10 not in s)
# 集合元素的新增操作
print('--------集合元素的新增操作---------')
s.add(27)
print(s)
s.update({200, 300, 400, 500})
print(s)
print('--------集合元素的删除操作---------')
s.remove(200)
print(s)
s.discard(500)
print(s)
s.pop()  # pop不能添加参数，是无参的
print(s)
s.clear()
print(s)
