
#UDP CLEINT PROGRAM

import socket

message_from_client = "helloserver"

encoded_data = str.encode(message_from_client)

server_adress_port = ("127.0.0.1", 7)

buffersize = 1024

UDPclient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPclient.sendto(encoded_data, server_adress_port)

message_from_server = UDPclient.recvfrom(buffersize)

msg = "Message from Server {}".format(message_from_server[0])

print (msg)