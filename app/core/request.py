#!/usr/bin/python3
import os
import urllib.request, urllib.parse, urllib.error
    
class Request(object):
    def __init__(self,env):
        self.reqvars={}
        for el in list(env.keys()):
            self.reqvars[el]=env[el]
        self.query={}
        self.post={}
        self.cookie=''
        #create a dict from querystring
        try:
            elems=self.reqvars['QUERY_STRING'].split('&')
            for x in elems:
                self.query[x.split('=')[0]]=x.split('=')[1]
        except:
            pass
        #create post dict from POST
        try:
            postelems=self.reqvars['POST'].split('&')
            for el in postelems:
                self.post[el.split('=')[0]]=el.split('=')[1]
        except:
            #get json object
            try:
                self.post['json']=self.reqvars['POST']
            except:
                pass
        try:
            self.cookie=self.reqvars["HTTP_COOKIE"]
        except:
            pass
    def getCookie(self):
        return self.cookie
            
    def getPost(self):
        return self.post
    
    def getGet(self):
        return self.query
#get GET dict            
    def GET(self,attr,default=''):
        try:
            return urllib.parse.unquote(self.query[attr])#.decode('utf8')
        except:
            return default
#get POST dict            
    def POST(self,attr,default=''):
        try:
            return urllib.parse.unquote(self.post[attr])#.decode('utf8')
        except:
            return default
    def addVar(self,var,val):
        self.reqvars[var]=val
#add variable to get dict        
    def addGETVar(self,var,val):
        self.query[var]=val

    def addPOSTVar(self,var,val):
        self.post[var]=val
    
    def getPath(self):
        if 'page' not in self.query:
            return 'root'
        return self.GET('page')
