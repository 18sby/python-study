# 在导入带有包的模块时注意事项

# 使用 import 进行导入时，只能跟包名或模块名
import package1
import calc

# 使用 from 进行导入，可以导入包、模块、函数/变量等
from package1 import moduleA
from package1.moduleA import a