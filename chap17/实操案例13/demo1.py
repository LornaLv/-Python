# Date: 2023/2/24 下午3:34
# 任务一：编写程序实现乐手弹奏乐器。乐手可以弹奏不同的乐器而发出不同的声音。可以弹奏的乐器包括二胡、钢琴和琵琶。
class Instrument(object):
    def make_sound(self):
        pass


class Erhu(Instrument):
    def make_sound(self):
        print('二胡在演奏')


class Piano(Instrument):
    def make_sound(self):
        print('钢琴在演奏')


class Vinion(Instrument):
    def make_sound(self):
        print('小提琴在演奏')


def player(instrument):
    instrument.make_sound()


class Bird():
    def make_sound(self):
        print('小鸟在唱歌')


if __name__ == '__main__':
    player(Erhu())
    player(Piano())
    player(Vinion())
    player(Bird())
