# Date: 2023/2/17 下午1:21
# key的判断
scores = {'张三': 100, '李四': 98, '王五': 67}
print('---------------key的判断----------------')
print('张三' in scores)
print('张三' not in scores)

print('---------------字典元素的删除----------------')
del scores['张三']
print(scores)
# scores.clear()
print(scores)

print('---------------字典元素的新增/修改----------------')
scores['陈柳'] = 100
print(scores)
