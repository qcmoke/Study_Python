class Cat:
    typeName = "小猫"

    def show(self, name):
        """1、普通方法
            特点是：普通方法的第一个参数是对象self(调用时可省略这个参数)，能访问类属性，也能访问对象属性，能访问普通方法等；只能通过对象调用
        """
        self.name = name
        print(Cat.typeName, self.name)

    # 注意：python不支持方法重载，如果有相同名称的方法，那么定义在后面的同名方法生效
    # def show(self, name, age):
    #     pass

    @classmethod
    def testClassMethod(cls):
        """2、类方法
            添加装饰器@classmethod的方法就是类方法，
            特点：类方法的第一个参数不是对象self而是类cls(调用时可省略这个参数)，只能访问类属性，不能访问对象属性，也不能访问普通方法等；只能通过类调用
        """
        print(cls.typeName)  # 等价于 print(Cat.typeName)

    @staticmethod
    def testStaticMethod():
        """3、静态方法(与类方法相似，不同点是类方法必须有第一个参数cls，而静态方法不需要)
            添加装饰器@staticmethod的方法就是静态方法，
            特点：静态方法可以无参数，只能访问类属性，不能访问对象属性，也不能访问普通方法等；能通过对象和类调用
        """
        print(Cat.typeName)

    def __init__(self, *args, **kwargs):
        """4、魔术方法
        详情参考：https://www.cnblogs.com/zhangboblogs/p/7860929.html
        定义：方法名前后有双下划线的方法，与其他方法不同的是，魔术方法不需要调用，在类或者对象的特定时刻自动触发
        常用魔术方法有：
            __foo__: 定义的是特殊方法，一般是系统定义名字 ，类似 __init__() 之类的。
           (1) __init__()
                初始化魔术方法
                触发时机：初始化对象时触发（不是实例化触发，但是和实例化在一个操作中）
                参数：至少有一个self，接收对象
                返回值：无
                作用：初始化对象的成员
                注意：使用该方式初始化的成员都是直接写入对象当中，类中无法具有
            (2)__new__()
            (3)__del__() 
            (4)__call__() 把对象当作函数使用
            (5)__len__()
            (6)__str__() 类似java的tostring()
            (7)__repr__()
            (8)__bool__()
            (9)__format__()
        """
        pass


# 调用普通方法，只能通过对象调用
Cat().show("tom")

# 调用类方法，只能通过类调用，调用的类会被传入到类方法的第一个参数中
Cat.testClassMethod()

# 调用静态方法，能通过对象和类调用
Cat.testStaticMethod()
Cat().testStaticMethod()
