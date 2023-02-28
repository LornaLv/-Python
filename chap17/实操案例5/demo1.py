# Date: 2023/2/23 下午4:26
# 任务一：循环输出26个字母对应的ASCII码值
x = 97  # 代表的是a的ASCII码值
for _ in range(1, 27):
    print(chr(x), '---->', x)
    x += 1
