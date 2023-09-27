import socket

host = 'localhost'
port = 12345

# Defina as perguntas do quiz e as respostas corretas
quiz_data = [
    {"pergunta": """1 - O que é um sistema distribuído aberto?
a) É um sistema que permite uma ampliação gradual de seus recursos
b) São sistemas de pequeno porte, alimentados por bateria
c) É um sistema que, por conter serviços e regras padronizadas, permite a comunicação entre aplicações de diferentes fornecedores
d) Nenhuma das opções""", "resposta_correta": "c)"},
    {"pergunta": """2 - O que se entende por escalabilidade de uma rede?
a) É o tempo decorrido após uma operação de envio ser executada
b) Capacidade de sua infraestrutura suportar o crescimento da rede
c) Capacidade da rede em garantir a correta entrega dos dados no destino
d) Capacidade de permitir que conversões ocorram somente se forem necessárias""", "resposta_correta": "b)"},
    {"pergunta": """3 - Qual o papel do middleware em um sistema distribuído?
a) Economia de recursos e compartilhamento de informações
b) Promover a comunicação entre os sistemas oferecendo a mesma interface para as aplicações
c) Para manter a independência entre os protocolos de cada camada
d) Prover um middleware padrão entre sistemas heterogêneos""", "resposta_correta": "b)"},
    {"pergunta": """4 - As linguagens XML e HTML possuem estrutura parecida, sendo essencialmente estruturada com a utilização de tags. O que os diferencia?
a) A XML especifica a estrutura dos dados, enquanto a HTML especifica o layout
b) A XML permite a criação de novas tags para uso pelas aplicações, enquanto HTML define um formato binário para representação de dados
c) A XML especiffica o layout, enquanto a HTML especifica a estrutura de dados
d) Nenhuma das opções""", "resposta_correta": "a)"},
    {"pergunta": """5 - O que é uma rede de sobreposição?
a) Rede formada por um conjunto de sensores que se comunicam para distribuição de informações
b) Rede onde os componentes trabalham um em prol do outro visando o cumprimento da tarefa
c) Rede responsável por manter a independência entre os protocolos de cada camada
d) Rede formada sobre outra rede, contendo apenas os nós e enlaces necessários ao funcionamento do sistema""", "resposta_correta": "d)"},
    {"pergunta": """6 - Qual a principal vantagem a ser obtida quando se monta um sistema distribuído para utilização em substituição a um sistema centralizado?
a) Somar o poder de processamento dos equipamentos na execução da tarefa.
b) Promover a comunicação entre os sistemas oferecendo a mesma interface para as aplicações.
c) Economia de recursos e compartilhamento de informações.
d) Garantir a integridade caso a aplicação não possa executar até o final.""", "resposta_correta": "a)"},
    {"pergunta": """7 - Em que a RMI é diferente da RPC?
a) RPC e RMI ocultam do programador aspectos importantes da distribuição, promovendo um elevado nível de transparência de acesso e de localização.
b) A RMI é voltada para invocação a métodos remotos (objetos) enquanto a RPC é baseada na comunicação entre processos por intermédio de chamadas de procedimentos.
c) A RMI é não voltada para invocação a métodos remotos (objetos) enquanto a RPC é baseada na interface de sistemas.
d) A RMI é voltada para banco de dados enquanto a RPC é baseada na comunicação entre processos por intermédio de chamadas de procedimentos.""",  "resposta_correta": "b)"},
    {"pergunta": """8 - Um dos objetivos de um sistema distribuído é permitir o acesso a recursos remotos. Por que isto é desejável?
a) Economia de recursos e coleta de informações.
b) Economia de recursos e restrições de informações.
c) Economia de recursos e compartilhamento de informações.
d) Disperdício de recursos e compartilhamento de informações.""",  "resposta_correta": "c)"},
    {"pergunta": """9 - O que é transparência de distribuição? Por que ela é desejada?
a) Capacidade de aparecer para o usuário como um sistema integrado. Quanto mais complexo for um sistema, maior será seu valor para aplicação.
b) Capacidade de aparecer para o usuário como um sistema de computação em nuvem. Quanto mais transparente for um sistema, mais fácil será de utilizá-lo.
c) Capacidade de se ocultar para o usuário como um sistema único. Quanto mais transparente for um sistema, maior será sua complexidade.
d) Capacidade de aparecer para o usuário como um sistema único. Quanto mais transparente for um sistema, mais fácil será de utilizá-lo.""",  "resposta_correta": "d)"},
    {"pergunta": """10 - Por que nem sempre é bom buscar a transparência total em um sistema distribuído?
a) Em determinadas situações (sistemas pervasivos, por exemplo) é melhor que o usuário saiba tratar-se de um sistema distribuído e conhecer suas limitações, sabendo assim o que esperar do sistema.
b) Usar a trasparência total pode tornar o sistema distribuído vulnerável.
c) Usar a trasparência total pode piorar a performance do sistema.
d) Usar a trasparência total pode aumentar o custo de desenvolvimento.
    """,  "resposta_correta": "a)"},
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
