# Date: 2023/2/21 下午6:08
import sys
print('-----------sys-----------')
print(sys.getsizeof(24))
print(sys.getsizeof(45))
print(sys.getsizeof(True))
print(sys.getsizeof(False))

import time
print('-----------time-----------')
print(time.time())
print(time.localtime(time.time()))

import urllib.request
print('-----------urllib-----------')
print(urllib.request.urlopen('http://www.baidu.com').read())