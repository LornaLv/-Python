# Date: 2023/2/21 下午6:30
import time

import schedule


def job():
    print('haha')


schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
