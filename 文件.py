# coding= utf-8
import sys
import shutil
import requests请求

aa = open("aa", "a+")
aa.write("/n \n18wom")
aa.close()
aa = open("aa")
test = aa.read()
print(test)
sys.stderr.write("文件没有关闭\n")
aa.close()
aa = open("aa")
while True:
    test = aa.readline()
    if not test:
        break
    print(test, end="结束")
aa.close()
print("hello")

print(eval("1+2"))


