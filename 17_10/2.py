import socket

sock = socket.socket()
HOST = ('127.0.0.1',7777)
sock.connect(HOST)
sock.send('1234567890'.encode('utf-8'))
sock.send('0987654321'.encode('utf-8'))