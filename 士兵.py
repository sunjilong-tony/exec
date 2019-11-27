# coding= utf-8
class Gun:
    def __init__(self, name):
        self.name = name
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count = count

    def shoot(self):
        # 判断是否有子弹
        if self.bullet_count <= 0:
            print("没有子弹了%s" % self.bullet_count)
            return
        self.bullet_count -= 1
        # 射击完成输出的内容
        print("射击完成,剩余%d" % self.bullet_count)


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None:
            print("新兵没有枪")
            return
        self.gun.add_bullet(50)
        self.gun.shoot()
ak47 = Gun("AK47")
xusan = Soldier("xu san duo")
xusan.gun = ak47
xusan.fire()



