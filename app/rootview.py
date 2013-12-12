#!/usr/bin/python3
from .core.response import HttpResponse
from .core.Templates.template import HtmlTemplate
from .templates.htmltemplate import htmlroot



def getRoot(req):
    hmtp=HtmlTemplate(htmlroot)
    rendtemp=hmtp.render({})
    resp=HttpResponse('Content-Type: text/html',rendtemp)
    resp.send()

