# Date: 2023/2/17 下午12:43
# 获取字典的元素
scores = {'张三': 100, '李四': 98, '王五': 67}
print('---------------第一种方式：使用[]----------------')
print(scores['张三'])
# print(scores['liu']) #KeyError
print('---------------第二种方式：使用get（）方法----------------')
print(scores.get(('张三')))
print(scores.get(('liu')))
print(scores.get('马奇', 99))
