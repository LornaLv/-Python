# Date: 2023/2/16 下午10:34

lst = [10, 20, 10, 78, 92, 40]
print('排序前的列表：', lst, id(lst))

# 开始排序，调用列表对象的sort方法，默认是升序排序
lst.sort()
print('排序后的列表：', lst, id(lst))

# 通过指定关键字参数，，将列表中的元素降序排序
lst.sort(reverse=True)
print('降序排序后的列表：', lst)

# 采用内置函数sorted（）排序，会产生新的列表对象
print('-------------sorted()----------------')
lst1 = [10, 20, 10, 78, 92, 40]
print('排序前的列表：', lst1, id(lst1))
new_list = sorted(lst1)
print('排序后的列表：', new_list, id(new_list))

# 指定关键字参数，实现列表的降序排序
lst2 = sorted(lst1, reverse=True)
print('降序排序后的列表：', lst2)
