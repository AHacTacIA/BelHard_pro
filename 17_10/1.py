import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = ('127.0.0.1',7777)
sock.bind(HOST)
sock.listen()
print('listen')

while True:
    conn, addr = sock.accept()
    data = conn.recv(1024).decode()
    # print(conn)
    # print(addr)
    print(data)
    print()