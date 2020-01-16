# 通过"from 模块名 import 内容" 的方式导入，特点是使用模块里的内容时不需要在内容前加"模块名."
# from utils import * #导入所有

from utils import num, test, User  # 按需导入

# 访问其他模块的变量
print(num)
# 访问其他模块的函数
test("hello")
# 访问其他模块的方法
User(101, "zhangsan").say()
