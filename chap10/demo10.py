# Date: 2023/2/19 下午10:53
# 递归函数
def fac(n):
    if n == 1:
        return 1
    else:
        res = n * fac(n - 1)
        return res


print(fac(6))
