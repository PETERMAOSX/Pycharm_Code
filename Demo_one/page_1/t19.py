from wsgiref.simple_server import make_server
def application(envion,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    return [b'<h1>Hello,web!</h1>']
httpd = make_server('',9000,application)
print("Serveing HTTP on prot 9000....")

httpd.serve_forever()
