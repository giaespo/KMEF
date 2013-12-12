#!/usr/bin/python3
import os
#dispatcher object, calls the right function based on page name
class Urls(object):
    def __init__(self,req):
        self.req=req
        
    def setUrls(self,path):
        self.path=path
        val= self.req.getPath()
        #try:
        if self.path['isValidSession'](self.req) or (val=='index'):
            self.path[val](self.req)
        else:
        	self.path['autoLogin'](self.req)
        	self.path[val](self.req)
            #self.path['404'](self.req,'sessione scaduta')
    


