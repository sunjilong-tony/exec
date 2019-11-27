# coding= utf-8
import json
def gender(name, sex=None):
    if sex is True:
        sex = "man"
    elif sex is False:
        sex = "women"
    print("%s is %s" % (name, sex))


gender("tony", True)



