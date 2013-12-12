#!/usr/bin/python3
import pickle
import os
from ... import settings

class Injection(object):
    def setField(self,field):
        self.field=field
    def run(self):
        pass

class Persistent(Injection):
    def __init__(self):
        #self._getPicklesVars()
        pass
    
    def deleteModelInfo(self,model=[]):
        for m in model:
            try:
                os.remove(settings.appFolder + settings.tmpFolder + m + '.dat')
            except Exception as e:
                pass
         
    def getVar(self,var):
        """ Get Variable """
        self._getPicklesVars(var.split('.')[0])
        result=''
        try:
            result= self.vars[var.split('.')[0]][var.split('.')[1]]
        except:
            pass
        return result
        
    def setVar(self,var,val):
        """ Test method, """
        try:
            self._getPicklesVars(var.split('.')[0])
        except:
            pass
        if not var.split('.')[0] in self.vars:
            self.vars[var.split('.')[0]]={}
        self.vars[var.split('.')[0]][var.split('.')[1]]=val
        
        self._savePicklesVars(var.split('.')[0])
        return val
        
    def delVar(self,var):
        """ Test method,  """
        self._getPicklesVars(var.split('.')[0])
        del self.vars[var.split('.')[0]][var.split('.')[1]]
        self._savePicklesVars(var.split('.')[0])
        return True
    
    def delMasterVar(self,var):
        self._getPicklesVars(var.split('.')[0])
        try:
            del self.vars[var]
            self._savePicklesVars(var.split('.')[0])
        except:
            pass
        return True
        
    def getvars(self,namefile):
        """ Test method,  """
        self._getPicklesVars(namefile)
        return self.vars
            
    def _getPicklesVars(self,namefile):
        try:
            self.vars = pickle.load(open(settings.appFolder + settings.tmpFolder + namefile + ".dat", "rb"))
        except:
            self.vars={}
    def _savePicklesVars(self,namefile):
        pickle.dump(self.vars,open(settings.appFolder + settings.tmpFolder + namefile +".dat", "wb" ))

    def run(self,var,val):
        self.setVar(var,val)
        #print self.getvars()

class FilterRights(Injection):

    def run(self,var,val):
        valu=[m['Id'] for m in val[0] if m['Enabled']==True]
        result=''
        for el in valu:
            result += str(el) + '-'
        if result:
            return result[:-1]
        else:
            return result

class Mailcounts(Injection):
 
    def run(self,var,val):
        res={}
        lsres=['tmc','umc','tmf','umf','tm','um','atd','aic']
        #valu=[m['Value'] for m in val[0]]
        for n in range(len(lsres)):
            res[lsres[n]]=val[0][n]['Value']#valu[n]
        return res

class FilterUsers(Injection):

    def run(self,var,val):
        return val[0]
        
class InputHtml(Injection):

    def renderHtml(self,field,cls,ident):
        return '<input class="' + cls + '" type="text" id="' + ident + '" name="' + field.name + '" value="' +  field.value + '"></input>'
        
    def run(self,var,val):
        self.field.setHtmlFunc(self.renderHtml)
        
class PasswordHtml(Injection):

    def renderHtml(self,field,cls,ident):
        return '<input class="' + cls + '" type="password" id="' + ident + '" name="' + field.name + '" value="' +  field.value + '"></input>'
        
    def run(self,var,val):
        self.field.setHtmlFunc(self.renderHtml)
        

class selectHtml(Injection):
    
    def renderHtml(self,field,cls,ident):
        val=''
        els=self.valore
        for el in els:
            val += '<option value="' + el + '">' + el + '</option>'
        return '<select class="' + cls +'" id="' + ident + '" name="domain">' + val + '</select>'
        
    def run(self,var,val):
        self.valore=val
        self.nome=var
        self.field.setHtmlFunc(self.renderHtml)
        return val
        

class tableHtml(Injection):
    
    def renderHtml(self,field,cls,ident):
        val=''
        els=self.valore
        val +='<tr><td>' + self.nome + '</td></tr>'
        for el in els:
            val += '<tr><td>' + el + '</td></tr>'
        return '<table border="1" class="' + cls +'" id="' + ident + '">' + val + '</table>'
        
    def run(self,var,val):
        self.valore=val
        self.nome=var
        self.field.setHtmlFunc(self.renderHtml)
        return val
