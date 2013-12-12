#!/usr/bin/python3
import json
from .metamodel import Metamodel

class Model(object, metaclass=Metamodel):
    def getJsonInput(self):
        values={}
        for el in self.input:
            values[el]=getattr(self, el).getValue()
        jsonrepr= self.jsontempl % values   
        return json.dumps(jsonrepr)
    def getJsonOutput(self):
        valuesout={}
        for el in self.output:
            valuesout[el]=getattr(self, el).getValue()
        jsonreprout= self.jsontemplout % valuesout   
        return json.dumps(jsonreprout)
    def getHTML(self,attr):
        return getattr(self, attr)._getHTML() % {'name':attr}
    def getAttrVal(self,attr):
        return getattr(self, attr).getValue()
    def getAttrName(self,attr):
        return getattr(self, attr).getName()

