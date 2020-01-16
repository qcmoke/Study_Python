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


class Student(Person):
    """学生"""

    def task(self):
        print("studying...")


class Employee(Person):
    """员工"""

    def task(self):
        print("working...")
