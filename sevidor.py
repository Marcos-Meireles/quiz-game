import socket

host = 'localhost'
port = 12345

# Defina as perguntas do quiz e as respostas corretas
quiz_data = [
    {"pergunta": """Qual é a capital da França?
    a) Paris
    b) Madrid
    c) Genova    
    """, "resposta_correta": "a)"},
    {"pergunta": "Qual é o maior planeta do sistema solar?", "resposta_correta": "Júpiter"},
    {"pergunta": "Quem escreveu 'Dom Quixote'?", "resposta_correta": "Cervantes"}
]


def start_quiz(conn):
    score = 0

    for question in quiz_data:
        conn.sendall(question['pergunta'].encode())
        resposta = conn.recv(1024).decode()

        if resposta.lower() == question["resposta_correta"].lower():
            score += 1

    conn.sendall(f"Sua pontuação final é: {score}/{len(quiz_data)}".encode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()

    print(f'Aguardando conexão em {host}:{port}')
    conn, addr = s.accept()
    print('Conexão de', addr)

    start_quiz(conn)

    print('Conexão encerrada.')
