# Date: 2023/2/17 下午1:29
scores = {'张三': 100, '李四': 98, '王五': 67}
print('---------------获取所有的键key----------------')
keys = scores.keys()
print(keys)
print(type(keys))
print(list(keys))  # 将所有键组成的视图转成列表

print('---------------获取所有的value----------------')
values = scores.values()
print(values)
print(type(values))
print(list(values))

print('---------------获取所有的键值对 key-value对----------------')
items = scores.items()
print(items)
print(type(items))
print(list(items))  # 转换后的列表元素是由元组组成的
