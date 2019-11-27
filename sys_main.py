# coding= utf-8

import sys_tool


while True:
    sys_tool.card_menu()
    choice = input("请输入您的选择(1新建名片2显示全部3查询名片):")
    print("您的选择是%s" % choice)
    if choice in ["1", "2", "3"]:
        if choice == "1":
            sys_tool.card_add()
        elif choice == "2":
            sys_tool.card_show()
        elif choice == "3":
            sys_tool.card_search()
    elif choice == "0":
        print("欢迎再次使用")
        break
    else:
        print("您输入的不正确，请重新选择")
