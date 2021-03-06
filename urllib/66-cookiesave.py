#!/usr/bin/env python 
# -*- coding:utf-8 -*

from urllib import request
from  http.cookiejar import  MozillaCookieJar

cookiejar = MozillaCookieJar('cookie.txt')
cookiejar.load(ignore_discard=True)

handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

resp = opener.open('http://www.httpbin.org/cookies/set?course=ASDF')
for cookie in  cookiejar:
    print(cookie)

# cookiejar.save(ignore_discard=True)
