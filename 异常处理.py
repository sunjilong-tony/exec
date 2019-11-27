# coding= utf-8
# try:
#     num = int(input("请输入一个整数： "))
#     result = 8 / num
# except Exception as error:
#     print("未知错误%s" % error)
#
# print("*" * 50)


def passwd():
    pwd = str(input("请输密码："))
    if len(pwd) > 8:
        return pwd
    error = Exception("密码长度不够用")
    raise error

try:
    print(passwd())
except Exception as errors:
    print("%s" % errors)



