# Date: 2023/2/17 下午1:38
# 字典元素的遍历
scores = {'张三': 100, '李四': 98, '王五': 67}
for item in scores:
    print(item, scores[item], scores.get(item))
