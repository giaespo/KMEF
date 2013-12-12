#!/usr/bin/python3
import urllib.request, urllib.error, urllib.parse

class Opener(object):
    def __init__(self,headers,site,payload,method,filedescr):
        self.headers=headers
        self.site=site
        self.payload=payload.encode('utf-8')
        self.meth=method
        self.filedescr=filedescr
        
    def _getOpener(self):
        proxy_handler = urllib.request.ProxyHandler({})
        return urllib.request.build_opener(proxy_handler)
        
    def requestResponse(self):
        req = urllib.request.Request(self.site, self.payload,self.headers)
        if self.meth:
            req.get_method = lambda: self.meth
        response = self._getOpener().open(req)
        return response

        
    def fileRequestResponse(self):
        import http.client
        #f2=open('/var/www/cgi-bin/datas3/pinuccio.txt','a')
        fil=open(self.filedescr,'rb')
        response=''
        
        conn = http.client.HTTPConnection(self.site.split('/')[2] + ':80')
        try:
            conn.request(self.meth,'/' + '/'.join(self.site.split('/')[3:]), fil, self.headers)
        except Exception as e:
         #   f2.write(str(e))	
            pass
        response = conn.getresponse()
        #f2.write(str(response.read()))
        #f2.close()
        return response
       
 
#site="http://192.168.139.91/ArchiflowService/Login.svc/json/getDomains"
#headers = {'Content-Type': 'application/json; charset=utf-8'}
#binary_data = ''.encode('utf-8')
#x=Opener(headers,site,binary_data)
#print(x.requestResponse().read())
