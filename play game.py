# coding= utf-8
class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳..." % self.name)


class XiaoTianDog(Dog):
    def game(self):
        super().game()
        print("%s 需要在天上玩耍" % self.name)


class Persion(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, Dog):
        print("%s 和%s 玩耍的很愉快" % (self.name, Dog.name))
        Dog.game()


wangcai = XiaoTianDog("旺财")
erlangshen = Persion("二郎神")
erlangshen.game_with_dog(wangcai)
print(dir(XiaoTianDog))