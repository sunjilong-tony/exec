# coding= utf-8
class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "%s 占地 %.1f 平方米" % (self.name, self.area)

bed = HouseItem("席梦思", 20)
chest = HouseItem("衣柜", 2)
table = HouseItem("桌子", 70)


class House:
    def __init__(self, house_type, area):
        """

        :param house_type: 选择房子的类型
        :param area:
        """
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return ("户型:%s\n总面积:%.1f\n剩余面积:%.1f\n家具列表:%s"
                % (self.house_type, self.area, self.free_area, self.item_list))

    def add_item(self, item):
        print("增加的%s" % item)
        if self.free_area < item.area:
            print("放不下了")
            return
        self.item_list.append(item.name)
        # 剩余面积的计算
        self.free_area -= item.area


house = House("2室一厅", 80)
house.add_item(bed)
house.add_item(table)
print(house)

