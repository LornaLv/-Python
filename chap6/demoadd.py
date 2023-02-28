# Date: 2023/2/16 下午9:58

lst = [10, 20, 30]
print('添加元素之前lst内容：', lst)
print('添加元素之前lst id：', id(lst))

# 向列表的末尾添加一个元素
lst.append(40)
print('添加元素之后lst内容：', lst)
print('添加元素之后lst id：', id(lst))

lst2 = ['hello', 'world']
# lst.append(lst2),将lst2做为一个元素添加到lst
lst.append(lst2)
print(lst)

# lst.extend(lst2),将lst2的每一个元素分别添加到lst的末尾
lst.extend(lst2)
print(lst)

# 在任意位置上添加一个元素,在1的位置添加元素90
lst.insert(1, 90)
print(lst)

lst3 = [True, False, 'hello']
# 在任意位置上添加至少一个元素
lst[1:] = lst3
print(lst)
