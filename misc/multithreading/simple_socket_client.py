import socket

HOST = "localhost"
PORT = 8888

#  Create socket (IPv4, stream-based, protocol likely set to TCP)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("client connected to to {}:{}!\n".format(HOST, PORT))
    string = b'Hello world!'
    s.sendall(string)
    print('Sent', string)
    data = s.recv(1024)
print('Received', repr(data))
