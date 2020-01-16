"""
子类属性和方法的查找原则：先查子类再查父类
"""


class Person:
    """人类"""

    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age

    def say(self):
        print("{}在说话".format(self.name))


class Student(Person):
    """学生"""

    def __init__(self, name, age, clazz):
        super().__init__(name, age)  # 由于父类的__init__()有对象属性的值形参，故一定要传入，否则无法初始化对象属性
        self.clazz = clazz

    def say(self, msg):  # 重写父类方法
        print("{}说了{}".format(self.name, msg))


class Teacher(Person):
    """教师"""

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def teach(self):
        print("在上课教书")


Student("zhangsan", 21, "软工1班").say("I am a good boy !")
Teacher("王老师", 31, 10000).say()
