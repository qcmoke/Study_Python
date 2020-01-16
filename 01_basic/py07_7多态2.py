class Dog:
    def move(self):
        print("小狗在跑")


class Cat:
    def move(self):
        print("小猫在爬树")


# 同一个pet对象能够执行不同实现的move()
pet = Dog()
pet.move()

pet = Cat()
pet.move()
