# 通过"import 模块名" 的方式导入，特点是使用模块里的内容时需要在内容前加"模块名."
import utils

# 访问其他模块的变量
print(utils.num)
# 访问其他模块的函数
utils.test("hello")
# 访问其他模块的方法
utils.User(101, "zhangsan").say()
