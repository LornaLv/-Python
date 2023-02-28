# Date: 2023/2/20 下午3:49
# print(10/0)

import traceback

try:
    print('-------------------')
    print(1 / 0)
except:
    traceback.print_exc()
