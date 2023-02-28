# Date: 2023/2/20 上午11:46
try:
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    result = a / b
    print('结果为：', result)
except ZeroDivisionError:
    print('除数不能为0哦！')
except ValueError:
    print('输入错误，只能输入数字串！')
print('程序结束')
