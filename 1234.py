# coding= utf-8
import pymysql
from urlib import request, parse
import muitlprocess

connect = pymysql.connect("192.168.112.10", "long", "long", "test")
cursor =  connect.cursor()
sql= "select * from names"
cursor.execute(sql)
cursor.fetchall()
connect.close()
# post get
#get
url= "http://www.baidu.com"
req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
data= resp.read()
print(data.encode("utf-8"))
#post
data={"name":"tony", "age":18}
data_Z= urllib.parse.urlencode(data)
req1= urllib.request.Request(url, data_Z)
resp1 = urllib.request.urlopen(req1, timeout=3).read()
print(resp1("utf-8"))
# add header
User_agent="Mozilla/5.0 (Windows NT 10.0; WOW64)" \
           " AppleWebKit/537.36 (KHTML, like Gecko) " \
           "Chrome/76.0.3809.100 Safari/537.36
"
headers = {”User-Agent“:User_agent}
data={"name":"tony", "age":18}
data_Z= urllib.parse.urlencode(data)
req1= urllib.request.Request(url, data_Z)
resp1 = urllib.request.urlopen(req1, timeout=3).read()
print(resp1("utf-8"))