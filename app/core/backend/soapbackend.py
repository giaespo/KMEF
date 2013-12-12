#!/usr/bin/python3
import json
from xml.etree import ElementTree
from ..transport.transport import Opener
from ...usersview import *
class Backend(object):
    def __init__(self,headers,site,payload,model,root=False,method="",filedescr=None):
        self.opener=Opener(headers,site,payload,method,filedescr)
        self.model=model
        self.root=root
        self.filedescr=filedescr
        import codecs
        
        
    def _getResponse(self):
        resp=''
        #val=dir[usersview]
        #f=open('/var/www/cgi-bin/datas3/dir.txt','w')
        #f.write(str(val))
        #f.close()
        #val=isValidSession([])
        #if val:
            
        if self.filedescr:
            resp=self.opener.fileRequestResponse()
        else:
            resp=self.opener.requestResponse()
        return resp
        
        
class SoapBackend(Backend):
    def getResponse(self):
        resp=self._getResponse()
        tree=ElementTree.fromstring(resp.read())
        leafwords=[]
        simpleElem=[]
        for el in self.model.output:
            leafwords.append(el)

        for nod in tree.findall('.//*'):
            nodo=nod.tag.split('}')[1]
            if nodo in leafwords:
                simpleElem.append({nodo:nod.text})
                getattr(self.model, nodo).setValue(nod.text)
        return simpleElem
        

class FileStreamBackend(Backend):
    def getResponse(self):
        resp=''
        try:
            resp=self._getResponse()
        except:
            pass
        return resp
		


class JsonBackend(Backend):
    def getResponse(self):
        leafwords=[]
        res=''
        try:
            resp=self._getResponse()
            res=resp.read().decode("utf-8")

        except Exception as e:
            
            res={"result":"errore connessione ai servizi"}
            return res
        #import codecs
        #f = codecs.open('/var/www/cgi-bin/datas3/esempiores.txt', "w", "utf_8")
        #f.write(str(res))
        #f.close()
        try:
            dictresp=json.loads(res)
        except Exception as g:
            return {"result":"errore connessione ai servizi"}
        self.leafwords=[]
        self.leafarray=[]
        self.results={}
        
        for el in self.model.output:
            if getattr(self.model, el).getFieldType()=="array":
                self.leafarray.append(el)
            else:
                self.leafwords.append(el)
        for elm in self.leafarray:
            if elm[:-1] in self.leafwords:
                self.leafwords.remove(elm[:-1])
        if self.root:
            self._firstparse(dictresp)
        else:
            self._parse(dictresp)
        for el in self.results:
            
            try:
                getattr(self.model, el).setValue(self.results[el])
            except Exception as e:
                pass
        self.model.jsonoutput=str(res)
        
        return self.results
    
    def _parse(self,d):
        if type(d)==type({}):
            for k in d:
                if k in self.leafwords:
                    self.results[k]=d[k]
                elif (k + 's') in self.leafarray:
                    if (k + 's') in self.results:
                        self.results[k + 's'].append(d[k])
                    else:
                        self.results[k + 's']=[d[k]]
                if type(d[k]) in (type({}),type([])):
                    self._parse(d[k])
        elif type(d)==type([]):
            for e in d:
                if type(e) in (type({}),type([])):
                    self._parse(e)


    def _firstparse(self,d):
        for el in d:
            if el in self.leafwords:
                self.results[el]=d[el]
        
