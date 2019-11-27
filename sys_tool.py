# coding= utf-8
card_list = []


def card_menu():
    print("*" * 50)
    print("欢迎使用【名片管理系统】V1.0\n\n"
          "1.新建名片\n"
          "2.显示全部\n"
          "3.查询名片\n\n"
          "0.退出系统")
    print("*" * 50)


def card_add():
    name = input("请输入您的名字：")
    phone = input("请输入您的电话：")
    qq = input("请输入您的qq：")
    mail = input("请输入您的邮箱：")
    card_dict = {"name": name,
                 "phone": phone,
                 "qq": qq,
                 "mail": mail}
    card_list.append(card_dict)
    print(card_dict)


def card_show():
    print("-" * 50)
    print("             显示所有的名片")
    for title in ["姓名", "电话", "QQ", "邮箱"]:
        print(title, end="\t\t")
    print(" ")
    if len(card_list) <= 0:
        print("\n暂无数据\n")
        return
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["mail"]))


def card_search():
    find_name = input("请输入您要查询的名字：")
    print("您要查询的的人为%s" % find_name)
    for card_dict in card_list:
        if find_name == card_dict["name"]:
            print("姓名\t\t", "电话\t\t", "QQ\t\t", "邮箱\t\t")
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                                card_dict["phone"],
                                                card_dict["qq"],
                                                card_dict["mail"]))
            deal_card(card_dict)
            break
    else:
        print("没有找到%s" % find_name)


def deal_card(find_dict):
    print(find_dict)
    persion_choose = input("请输入您的选择 1修改 2删除 0返回上一层")
    if persion_choose == "1":
        find_dict["name"] = card_input(find_dict["name"], "姓名：")
        find_dict["phone"] = card_input(find_dict["phone"], "电话：")
        find_dict["qq"] = card_input(find_dict["qq"], "qq:")
        find_dict["mail"] = card_input(find_dict["mail"], "mail:")
        print("修改成功")
    elif persion_choose == "2":
        card_list.remove(find_dict)
        print("删除成功")


    """

    :param values:
    :param altervalues:
    :return:
    """


def card_input(values, altervalues):
    result_str = input(altervalues)
    if len(result_str) > 0:
        return result_str
    else:
        return values



