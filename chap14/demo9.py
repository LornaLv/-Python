# Date: 2023/2/21 下午5:58
#导入带有包的模块时的注意事项
import package1
import calc
# 使用import方式进行导入时，只能跟包名或者模块名
from package1 import module_A
from package1.module_A import a
# 使用from....import的形式，可以导入包、模块、函数变量