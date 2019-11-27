# coding= utf-8
class MusicPlayer(object):
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # print("分配空间")
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if MusicPlayer.init_flag:
            return
        print("初始化")
        MusicPlayer.init_flag = True

player = MusicPlayer()
print(player)
player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)