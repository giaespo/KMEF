#!/usr/bin/python3
from .injected import Injection



class SingletonPersistence(Injection):
    _instance = None

    def __init__(self):
        self.vars={}
        
    def setCookie(self,cookie):
        self.vars=cookie
        
    def delCookies(self):
        for el in self.vars:
            self.vars[el]=''
         
    def getVar(self,var):
        """ Get Variable """
        result=''
        try:
            result= self.vars[var].value 
        except Exception as e:
            pass
        return result
        
    def setVar(self,var,val):
        """ Test method, """
        self.vars[var]=str(val)
        return val
        
    def delVar(self,var):
        """ Test method,  """
        del self.vars[var]
        return True
    
    def delMasterVar(self,var):
        try:
            del self.vars[var]
        except:
            pass
        return True
        
    def getvars(self):
        """ Test method,  """
        return self.vars
       
    def run(self,var,val):
        self.setVar(var,val)



def SoftPersistence():
    if not SingletonPersistence._instance:
        SingletonPersistence._instance = SingletonPersistence()
    return SingletonPersistence._instance



#b = SoftPersistence()
#b.run('user.ciao','mondo')
 
#c = SoftPersistence()
#print(b.getvars())
#print(c.getVar('user.ciao'))
#d = SoftPersistence()


