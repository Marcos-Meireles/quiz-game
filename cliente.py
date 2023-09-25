import socket

host = 'localhost'
port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    cont = 0
    while True:
        question = s.recv(1024).decode()
        if not question:
            break

        print(f"Pergunta: {question}")

        resposta = input('Sua resposta: ')
        s.sendall(resposta.encode())
        cont+=1

    resultado = s.recv(1024).decode()
    print(resultado)
