# Date: 2023/2/21 下午9:26
# 要求列出指定目录下所有的python文件
import os

path = os.getcwd()  # 获取当前目录
lst = os.listdir(path)  # 获取这个路径下的所有文件
for filename in lst:
    if filename.endswith('.py'):
        print(filename)
