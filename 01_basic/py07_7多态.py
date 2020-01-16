import abc


class Person:
    """人类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 定义统一抽象方法,子类则必须重新实现该方法
    @abc.abstractmethod
    def task(self):
        pass

    # def test(self, peo):
    #     if isinstance(peo, Person):  # 判断peo是否属于Person类的对象
    #         pass


class Student(Person):
    """学生"""

    def task(self):
        print("studying...")


class Employee(Person):
    """员工"""

    def task(self):
        print("working...")


# 多态性，一种调用方式，不同执行效果
# 定义统一多态接口
def func(obj):
    obj.task()


student = Student("zhangsan", 21)
employee = Employee("mayun", 21)
func(student)
func(employee)
