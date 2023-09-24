import socket

host = 'localhost'
port = 10999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()

    conn, addr = s.accept()
    with conn:
        print('Conexão de', addr)
        data = conn.recv(1024)
        conn.sendall(data)
