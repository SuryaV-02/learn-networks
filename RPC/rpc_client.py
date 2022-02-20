from xmlrpc.client import ServerProxy

client = ServerProxy('http://localhost:8000')

for i in range(5):
    num1 = int(input('Enter Num 1 : '))
    num2 = int(input('Enter Num 2:  '))
    print('Addition : {}'.format(client.add(num1,num2)))
    print('Difference : {}'.format(client.sub(num1,num2)))
    print('Multiply : {}'.format(client.multi(num1,num2)))
    print('Divide : {}'.format(client.div(num1,num2)))
    print('Modulus  : {}'.format(client.mod(num1,num2)))
