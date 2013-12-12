#!/usr/bin/python3
class Metamodel(type):
    def __new__(meta, name, bases, dct):
        if name=='Model':
            return super(Metamodel, meta).__new__(meta, name, bases, dct)
        atrr=dct['input']
        jsontempl='{'
        for x in atrr:
            dct[x]=dct['input'][x]
            jsontempl += x + ':%(' + x + ')s,'
        jsontempl=jsontempl[:-1]
        jsontempl += '}'
        dct['jsontempl']=jsontempl
        
        outattr=dct['output']
        jsontemplout='{'
        for el in outattr:
            dct[el]=dct['output'][el]
            jsontemplout += el + ':%(' + el + ')s,'
        jsontemplout=jsontemplout[:-1]
        jsontemplout += '}'
        dct['jsontempl']=jsontempl
        dct['jsontemplout']=jsontemplout
        dct['jsonoutput']=''

        return super(Metamodel, meta).__new__(meta, name, bases, dct)
    def __init__(cls, name, bases, dct):
        super(Metamodel, cls).__init__(name, bases, dct)



