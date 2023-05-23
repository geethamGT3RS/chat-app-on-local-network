
#udp server

import socket

import sys

print ("sys.argv1 = ", sys.argv[1])

localip="192.168.0.105"

localport = int(sys.argv[1])

buffersize=1024

UDPserver = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPserver.bind((localip, localport))

messagefromserver="hello"

encodeddata=str.encode(messagefromserver)

print ("Server Ready and Binded on port No",localport)

while(True):

    bytesaddresspair = UDPserver.recvfrom(buffersize)

    message = bytesaddresspair[0]

    address = bytesaddresspair[1]

    clientMsg = "Message from Client:{}".format(message)
    
    clientIP  = "Client IP Address:{}".format(address)
    
    print(clientMsg)
    
    print(clientIP)

   
    UDPserver.sendto(encodeddata, address)


