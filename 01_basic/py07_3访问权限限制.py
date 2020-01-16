"""
访问权限限制
    包括：1.属性访问权限限制、2.方法访问权限限制
    分类：
        1.公有成员：
            前面没有下划线的成员。允许这个类本身和类外界进行访问了。
        2.私有成员:
            __foo: 双下划线的表示的是私有类型(private)的变量, 只能是允许这个类本身进行访问了。

        3.保护成员:
            _foo: 以单下划线开头的表示的是 protected 类型的变量，即保护类型只能允许其本身与子类进行访问，不能用于 from module import *
"""


class Cat:
    publicProp = ""  # 公有类属性
    __privateProp = ""  # 私有类属性
    _protected = ""  # 受保护的类属性

    def __init__(self, parm1, parm2, parm3):
        self.parm1 = parm1  # 公有类属性
        self.__parm2 = parm2  # 私有对象属性
        self._parm3 = parm3  # 受保护的对象属性

    def publicMethod(self):
        """共有方法"""
        pass

    def __privateMethod(self):
        """私有方法"""
        pass

    def _protectedMethod(self):
        """受保护的方法"""
        pass

    def get__privateProp(self):
        return self.__privateProp
