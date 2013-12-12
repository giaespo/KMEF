#!/usr/bin/python3
from .plugin.softpersistent import SoftPersistence
import json
#create a field object, 
class Field(object):
    def __init__(self,name,default,persist=None,injected=[]):
        self.name=name
        self.injected=injected
        if persist:
            self.persistence=persist()
            #self.injected.append(persist)
            
        self.value=default
        self.htmlCreator=self._createHtml
        
    def getFieldType(self):
        return 'string'
                
    def getValue(self):
        if self.name.startswith('key'):
            p=SoftPersistence()
            self.value=p.getVar(self.name.split('@')[1])
        elif len(self.name.split('.'))>1:
            self.value=self.persistence.getVar(self.name)
        return self.value
        
    def _createHtml(self,field,cls,ident):
        return "<div></div>"
    
    def getName(self):
        return self.name
        
    def setHtmlFunc(self,func):
        self.htmlCreator=func
        
    def _setValue(self,val):
        if self.name.startswith('key'):
            p=SoftPersistence()
            self.value=p.setVar(self.name.split('@')[1],val)
        elif len(self.name.split('.'))>1:
            self.value=self.persistence.setVar(self.name,val)
        else:
            self.value=val    
        
    def setValue(self,val):
        if self.name.startswith('key'):
            p=SoftPersistence()
            self.value=p.setVar(self.name.split('@')[1],val)
        elif len(self.name.split('.'))>1:
            self.value=self.persistence.setVar(self.name,val)
        else:
            self.value=val
        self._runInjected()
        
    def getInjected(self):
        return self.injected
        
    def _runInjected(self):
        inj=self.getInjected()
        val=self.value
        for el in inj:
            elm=el()
            elm.setField(self)
            val=elm.run(self.name,val)
        self._setValue(val)
            
            
class StringField(Field):
    def getHTML(self,cls,ident):
        return self.htmlCreator(self,cls,ident)

class PasswordField(Field):
    def getHTML(self,cls,ident):
        return self.htmlCreator(self,cls,ident)

class ArrayField(Field):
    def getFieldType(self):
        return 'array'
        
    def getHTML(self,cls,ident):
        return self.htmlCreator(self,cls,ident)

class DictField(Field):
    def getFieldType(self):
        return 'dict'
    
    def setValue(self,key,val):
        valu=self.getValue()
        if type(valu)==type({}):
            self.value=valu
        else:
            self.value={}
        self.value[key]=val
        self.value=self.persistence.setVar(self.name,self.value)
