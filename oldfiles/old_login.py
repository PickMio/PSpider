# -*- coding: utf-8 -*-
import urllib.request
import urllib.parse
from urllib.error import HTTPError, URLError
import http.cookiejar
LoginPage = "https://www.secure.pixiv.net/login.php"

header_dic = {
        "ContentType" : "application/x-www-form-urlencoded",\
        "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0",\
        "Referer" : "https://www.secure.pixiv.net/login.php",\
        "Accept" : "test/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",\
        "Accept-Language" : "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",\
       # "Accept-Encoding" : "gzip, deflate",\
        "Connection" : "keep-alive",\
        "Content-Length" : 47,\
        "Cache-Control" : "max-age=0",\
        "DNT" : "1"  
}

post_data = {
        "mode" : "login",\
        "pixiv_id" : "pickmio",\
        "pass" : "jxp2580",\
        "skip" : "1"
}

DATA = urllib.parse.urlencode(post_data)
DATA = DATA.encode(encoding='utf-8')

class HTTPRedirectHandler(urllib.request.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        print("Redirect is called but I get it")
        print("msg:", msg)
        param = headers.get("Set-Cookie")
       
        print("param:", param[0], param[1])
url = urllib.request.Request(url=LoginPage,data=DATA,headers=header_dic,method='POST')
'''
try :
        response = urllib.request.urlopen(url)
except HTTPError as e:
        print(e.code, e.reason)
web = response.readline()
print(response.code)
print(response.reason)
print(web.decode('utf8'))
#html = open("pixiv.html", 'wb+')
#html.write(web)
print(response.info())
'''

redHandler = urllib.request.HTTPRedirectHandler()
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj) , HTTPRedirectHandler())
try:
    web = opener.open(url)
except HTTPError as e:
    print(e)
'''    
print("headers:")
print("return code is", web.code)
print(web.info())
print(web.geturl())
print("cookie:")
cook = cj.make_cookies(web, url)
for item in cook:
    print(item)
'''
