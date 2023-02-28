# Date: 2023/2/16 下午10:10

lst = [10, 20, 30, 40, 50, 60, 30]
print('移除元素之前lst内容：', lst)
print('移除元素之前lst id：', id(lst))

# remove：从列表中移除一个元素，如果有重复元素，只移除重复元素的第一个元素
lst.remove(30)
print('移除元素之后lst内容：', lst)
print('移除元素之后lst id：', id(lst))

# pop：根据索引移除元素
lst.pop(1)
print(lst)
# pop:若不指定参数，则删除列表中的最后一个元素
lst.pop()
print(lst)

print('----------切片操作-删除至少一个元素、但是将产生一个新的列表对象----------')
new_lst = lst[1:3]
print('原列表：', lst, '原列表id：', id(lst))
print('新的列表：', new_lst, '新列表id：', id(new_lst))

print('----------不产生新的列表对象，而是删除原列表的内容----------')
lst[1:3] = []
print(lst)

# clear：清楚列表中的所有元素
lst.clear()
print(lst)

# del:将整个列表对象删除
del lst
print(lst)
