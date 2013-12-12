#!/usr/bin/python3
from string import Template
from ..plugin.injected import Persistent
from ...languages.lang import languages


base={'template':"""
<html>
  <head>
    ${title}
    ${link}
    ${js}
  </head>
  <body>
    ${navbar}
    ${content}
    ${footer}
  </body>
</html>

"""
}

header={
        'extend':base,
        'title':"""<title> We5! Il blog della guida HTML5 </title>""",
        
        
        'link':"""<link rel="stylesheet" type="text/css" href="mystyle.css"> """,
    
        'js':"""<script src="web-link.js"></script> """

       }
       
default={
      'extend':header,
      'navbar':"""<h1>navbar</h1>""",
      'content':"""<h2>Content </h2>""",
      'footer':"""<h3>footer</h3> """
      }


class SimpleTemplate(object):
    def __init__(self,template,model):
        self.template=template
        self.values={}
        for f in model.input:
            self.values[f]=model.getAttrVal(f)
        
    def render(self):
        return self.template % self.values
        
    def setTemplate(self,templ):
        self.template=templ
        
    def setValues(self,values):
        self.values=values



class HtmlTemplate(object):
    def __init__(self, template):
        self.template=template
        self.values={}
        
    def render(self,values):
        self.values=values
        while 'extend' in self.template:
            templ=self.template['extend']
            del self.template['extend']
            self.values.update(self.template)
            self.template=templ
        p=Persistent()
        #lang='it'
        lang=p.getVar('Impostazioni.language')			
        if not lang:
            lang='it'
        self.values.update(languages[lang])               
        return Template(self.template['template']).safe_substitute(self.values)
