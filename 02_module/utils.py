# 如果没有_定义_all__变量，则默认模块内所有内容都可以访问，添加__all__=['变量名称','函数名称','类名称']后则可以限制from utils import * 这种情况的访问
__all__ = ['num', 'test']

num = 100


def test(msg):
    print(msg)


class User:
    def __init__(self, uid, name):
        self.id = uid
        self.name = name

    def say(self):
        print(self.name)


# 为了避免在其他模块中导入当前模块时，自动执行语句，应该将当前模块中的执行语句放到"__name__"的判断体里,__name__的值分为两种情况，如果在执行当前模块，那么__name__值为__main__，否则值为当前所在的模块名
# print(num)
if __name__ == "__main__":
    print(num)
