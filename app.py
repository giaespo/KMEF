#!/usr/bin/python3

from app.core.request import Request
from app.core.url import Urls
from app.core.plugin.softpersistent import SoftPersistence
from app.rootview import getRoot


from app.core.views import get404
import http.cookies
import sys
import os
#import mfp
#import mfp.job
#import mfp.device

cookie=http.cookies.SimpleCookie()
#Verify Cookies existence
try:
    cookie = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
except (Exception) as e:
    pass
#insert cookies in singleton 
p=SoftPersistence()
p.setCookie(cookie)
        

#get all post data
postdata=sys.stdin.read()
env=os.environ
env['POST']=postdata
#create request passing a dict with all post, get and json data
req=Request(env)

#create Dispatcher passing the request
urls=Urls(req)

#the url of application, use this with app.py?page=x
newUrls={
         'root':index,
         'run':runsub,
         'index':index,
         'language':setLanguage,
         
         
         #page not found
         '404' : get404
        }
#pass urls to dispatcher
urls.setUrls(newUrls)

