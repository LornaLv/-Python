# Date: 2023/2/21 下午8:45

'''
MyContentMgr实现了特殊方法__enter()__和__exit()__
则称为该类遵守了上下文管理器协议
那么该类对象的实例对象酒称为上下文管理器
'''


class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用执行了')

    def show(self):
        print('show方法被调用执行了')


with MyContentMgr() as file:  # 相当于file=MyContentmgr()
    file.show()
