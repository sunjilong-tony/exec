# coding= utf-8
# class Cat:
#     def eat(self):
#         print("%s like 0" % self.name)
#     def drink(self):
#         print("cat like1")
# tom = Cat()
# tom.name = "tom"
# tom.drink()
# tom.eat()
# lazy_cat = Cat()
# lazy_cat.name = "大懒猫"
# lazy_cat.eat()
# lazy_cat.drink()


class CCC:
    def __init__(self, new_name):
        self.name = new_name
    def __str__(self):
        return "%s hahah" % self.name
    def __del__(self):
        print("game over")
    def eat (self ):
        print("%s 爱吃鱼" % self.name)
    def __new__(cls, *args, **kwargs):
        print("1111")
        return super().__new__(cls)



tom = CCC("ai永明")
print(tom)
tom.eat()
