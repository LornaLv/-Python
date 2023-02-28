# Date: 2023/2/23 下午5:19
# 计算100-999之间的水仙花数

print('------------方法一-----------')
for i in range(100, 999):
    ge = i % 10
    shi = int((i / 10) % 10)
    bai = int(i / 100)
    if ge * ge * ge + shi * shi * shi + bai * bai * bai == i:
        print(i)

print('------------方法二-----------')
import math

for i in range(100, 999):
    if math.pow((i % 10), 3) + math.pow((i // 10 % 10), 3) + math.pow(i // 100, 3) == i:
        print(i)
