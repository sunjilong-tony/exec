# coding= utf-8
try:
    num = int(input("请输入整数"))
    result = 8 / num
except ValueError:
    print("请输入整数")
except Exception as errors:
    print("未知错误%s" % errors)
else:
    print("结果： %s" % result)
finally:
    print("game over")


# class Animnal(object):
#     instance = None
#     init_flag = False
#
#     def __new__(cls, *args, **kwargs):
#         if cls.instance is None:
#             cls.instance = super().__new__(cls)
#         return cls.instance
#
#     def __init__(self, name):
#         if Animnal.init_flag:
#             return
#         Animnal.init_flag = True
#         self.name = name
#         self.age = 0
#
#     def __str__(self):
#         print("Type is %s " % self.name)
#
#     def eat(self):
#         print("吃东西")
#
#     def drink(self):
#         print("喝水")
#
#
# class Dog(Animnal):
#     def dirk(self):
#         print("叫的声音")
#
#
# class Xiaotianquan(Dog):
#     def wang(self):
#         super().dirk()
#         print("@@$#@#@")
#
# erlangshen = Xiaotianquan("erlangshen")
# erlangshen.wang()







