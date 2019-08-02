class Person:
    """人类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print("{}在说话".format(self.name))


class Student(Person):
    """学生"""

    def __init__(self, name, age, clazz):
        Person.__init__(self, name, age)  # 注意，对于多重继承，调用父类的__init__()方法，使用super().__init__()会报错，应该使用类名来调用
        Person.say(self)
        self.clazz = clazz

    def say(self, msg):
        print("{}说了{}".format(self.name, msg))

    def study(self):
        print("{}在{}学习".format(self.name, self.clazz))


class Employee(Person):
    """员工"""

    def __init__(self, name, age, company):
        Person.__init__(self, name, age)
        self.company = company

    def work(self):
        print("{}在{}上班工作".format(self.name, self.company))


class Trainee(Student, Employee):
    """实习生"""

    def __init__(self, name, age, clazz, company):
        Student.__init__(self, name, age, clazz)
        Employee.__init__(self, name, age, company)


te = Trainee("zhangsan", 21, "软工1班", "阿里巴巴")
te.study()
te.work()
