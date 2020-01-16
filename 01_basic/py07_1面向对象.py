'''
面向对象之类
    类包含两个元素：
        (1) 成员属性：用于描述类的特征的变量就是成员属性
        (2) 成员方法:用于描述类的特征的变量就是成员属性(不同于函数，方法属于类或者对象，而函数不属于)
                分类：
                    普通方法
                    类方法：
                    静态方法：
                    魔术方法：

    概念：
        1. 类变量和实例变量
        2. 类对象和实例对象
            类对象：类定义完成后，会在当前作用域中定义一个以类名为名字，指向类对象的名字，类对象主要是用来实例化对象
            实例对象：是类对象实例化的产物，实例对象仅支持一个操作：
        3. 属性绑定
        类属性绑定：类名.attr = attr_value
        实例属性绑定： self.attr = attr_value
        4. 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个self（self代表类的实例而非类），在调用时不必传入self相应的数。

    
    对象属性和方法的查找原则：先查对象再查类模板 
'''


class Cat:
    typeName = "小猫"  # 类变量（所有实例共享）

    # __init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
    def __init__(self, name, color, age):
        """初始化数据"""
        self.name = name  # self.name是实例变量 (每个单独实例共享)
        self.color = color
        self.age = age

    def show(self):
        """显示说明小猫的特征"""
        print("一只%s,品种为%s,毛色为%s,年龄为%d" %
              (Cat.typeName, self.typeName, self.color, self.age))  # 注意这里可以区分类变量和实例变量

    def eat(self, food):
        """喂养小猫吃食物"""
        print("%s吃了%s" % (self.name, food))

    def sleep(self, time):
        """小猫的睡眠时间"""
        print("%s睡了%sh" % (self.name, time))


cat1 = Cat("tom", "white", 1)
cat1.typeName = "英国短毛猫"  # cat1.typeName是实例变量 (每个单独实例共享)
cat1.show()
cat1.eat("小鱼")
cat1.sleep(2)

print("--" * 10)


cat2 = Cat("jeck", "black", 1)
cat2.typeName = "波斯猫"
cat1.show()
cat2.eat("饼干")
cat2.sleep(2)
