# coding= utf-8
class Demo:
    def __init__(self, new_name, weight):
        self.name = new_name
        self.weight = weight

    def __str__(self):
        return "%s 爱吃鱼" % self.name
        print("lalaaal")                  # 代码不会被执行

    def eat(self):
        print("%s 爱吃鱼% .2f" % (self.name, self.weight))
tom = Demo("tom", 70)
tom.eat()
print(tom)
tom.eat()