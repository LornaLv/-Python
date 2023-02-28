# Date: 2023/2/23 上午11:07
# 任务二：输出《红楼梦》中金陵十二钗前五位
print('------------第一种方式：变量的赋值--------------')
name1 = '林黛玉'
name2 = '薛宝钗'
name3 = '贾元春'
name4 = '贾探春'
name5 = '史湘云'
print('(1)\t' + name1)
print('(2)\t' + name2)
print('(3)\t' + name3)
print('(4)\t' + name4)
print('(5)\t' + name5)

print('------------第二种方式--------------')
lst_name = ['林黛玉', '薛宝钗', '贾元春', '贾探春', '史湘云']
lst_sig = ['(1)', '(2)', '(3)', '(4)', '(5)']
for i in range(5):
    print(lst_sig[i], lst_name[i])

print('------------第三种方式：字典--------------')
d = {'(1)': '林黛玉', '(2)': '薛宝钗', '(3)': '贾元春', '(4)': '贾探春', '(5)': '史湘云'}
for key in d:
    print(key, d[key])

print('------------第四种方式：zip--------------')
for s, name in zip(lst_sig, lst_name):
    print(s, name)
