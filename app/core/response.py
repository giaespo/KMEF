#!/usr/bin/python3
import http.cookies
#import datetime
import codecs
import sys
from .plugin.softpersistent import SoftPersistence
#create the response object
class HttpResponse(object):
    def __init__(self,header='',content=''):
        self.header=header
        self.content=content
        p=SoftPersistence()
        self.cookies=http.cookies.SimpleCookie()
        if p.getvars():
            self.cookies=p.getvars()
        
    def send(self):
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
        print(self.header)
        if self.cookies:
            try:
                print(self.cookies.output())
            except:
                pass
        print('')
        print(self.content)
        #print self.cookies.output()
        #for x in self.cookies: 
        #    print x,self.cookies[x].value   

    
