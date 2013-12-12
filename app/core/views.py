#!/usr/bin/python3
#standard 404 page, it prints page not found, the httpheader and the error not catched
def get404(req,e):
    print('Content-Type: text/html')
    print('') 
    print('<html>')
    print('<head><title>Pagina inesistente</title></head>')
    print('<body>')
    print('Pagina inesistente')
    print('<h1>ERRORE 404</h1>')
    print(str(req.reqvars))
    print('errore')
    print(str(e))
    print('<h2>Archiflow KM</h2>')
    print('</body></html>')
