from xmlrpc.server import SimpleXMLRPCServer

def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return abs(num1-num2)
def multi(num1,num2):
    return num1*num2
def div(num1,num2):
    return round(num1/num2,2)
def mod(num1,num2):
    return num1%num2

server = SimpleXMLRPCServer(('localhost',8000))
server.register_function(add,'add')
server.register_function(sub,'sub')
server.register_function(multi,'multi')
server.register_function(div,'div')
server.register_function(mod,'mod')

server.serve_forever()