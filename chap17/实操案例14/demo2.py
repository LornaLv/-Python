# Date: 2023/2/24 下午6:09
# 任务二：推算几天后的日期
import datetime


def inputdate():
    indate = input('请输入开始日期(按照20220808格式)后按回车：')
    indate = indate.strip()  # 去空格
    datestr = indate[0:4] + '-' + indate[4:6] + '-' + indate[6:8]
    return datetime.datetime.strptime(datestr, '%Y-%m-%d')


if __name__ == '__main__':
    print('----------推算几天后的日期----------')
    sdate = inputdate()
    in_num = int(input('请输入间隔的天数：'))
    fdate = sdate + datetime.timedelta(days=in_num)
    print('您推算的日期为：' + str(fdate).split(' ')[0])
