# coding= utf-8


class Persons:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.hight = 175

    # def __str__(self):
    #     return "%s like looking book ,her weight is %.2f" % (self.name, self.weight)

    def eat(self):
        self.weight += 50
        print("%s like me ,but he is weight %.2f" % (self.name, self.weight))

    def like(self):
        print("%d" % self.weight)

liky = Persons("liky", 75)
print(liky)

liky.like()
liky.eat()

wo = []
