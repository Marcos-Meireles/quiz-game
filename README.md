# Introdução

   Jogo no estilo Quiz (perguntas e respostas) criado com o conceito de Programação Distribuída e utilização da linguagem de programação Python. O Quiz consiste em um jogo de perguntas e respostas, onde teremos uma banca de 10 (dez) questões referentes ao conteúdo de aprendizagem referente a Programação Distribuída, onde a cada pergunta realizada será apresentado 4 (quatro) modelos de resposta sendo apenas 1 (um) correto(a). 
   Ao realizar a ação de "clicar" na resposta em que se deseja, a questão ficará marcada indicando qual será respondida, permitindo que o usuário possa clicar em outro botão chamado "Enviar", que será responsável por alterar entre as demais questões, possibilitando a opção de "avançar" para próxima questão.
   Ao responder todas as questões indicadas no Quiz, o usuário poderá finalizar sua tentativa, onde será exibido seu resultado durante o Quiz, na formatação preenchimento (exemplo: 4/10), possibilitando uma nova tentativa ou fechamento do Quiz.

# Arquitetura utilizada

  Para o funcionamento do projeto, foi utilizada a conexão cliente - servidor através da programação via socket, para um cliente comunicar-se com o servidor e trocar mensagens entre eles. O tipo de conexão escolhido foi o TCP, devido a sua conexão orientada ao fluxo de dados.

![image](https://github.com/Marcos-Meireles/quiz-game/assets/82594356/01c36b6f-80ba-45d1-afdd-5559c7cdf68b)


# Estruturação da solução do Sistema Distribuído



### Servidor

De início, o servidor é iniciado e fica esperando em loop infinito esperando a conexão com o cliente. 
Para a conexão, foi utilizada a biblioteca própria para a conexão via socket onde é colocado as variáveis do host e a porta a ser utilizada, nesse caso em específico, é possível colocar a string 'localhost' para pegar o ip do host local. A porta definida foi a 12345.
```python
import socket
import tkinter as tk

host = 'localhost'
port = 12345
```
Para estabelecer a conexão do servidor, é usada a função socket com os parâmetros AF_INET (para definir a família de endereço ipv4) e SOCK_STREM para mostrar que a conexão orientada no protocolo TCP e sendo armazenada na variável s.

Dentro do with, é feito o bind para poder vincular o ip e a porta ao servidor, para depois é usada a função listen() para colocar o servidor em modo de escuta. 

Dentro das variáveis conn e addr serão armazenadas as informações de conexão com do cliente para assim inicar o jogo na função start_quiz.

Após os rituais do jogo, a conexão automaticamente é encerrada.

```python
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()

    print(f'Aguardando conexão em {host}:{port}')
    conn, addr = s.accept()
    print('Conexão de', addr)

    start_quiz(conn)

    print('Conexão encerrada.')
```

### Cliente

Para a conexão, foi utilizada a biblioteca própria para a conexão via socket onde é colocado as variáveis do host e a porta a ser utilizada, nesse caso em específico, é possível colocar a string 'localhost' para pegar o ip do host local. A porta definida foi a 12345.
```python
import socket
import tkinter as tk

host = 'localhost'
port = 12345
```
Para estabelecer a conexão com o servidor, é usada a função socket com os parâmetros AF_INET (para definir a família de endereço ipv4) e SOCK_STREM para mostrar que a conexão orientada no protocolo TCP e sendo armazenada na variável s.

A função `connect()` estabelece a conexão com o servidor passando o host e a porta requisitada.

Após o início da conexão, é iniciada a função `tela_inicio()` para apresentar o jogo.

Dentro do loop infinito, é armazenada dentro da variável question a mensagem do servidor com as perguntas do jogo que serão mostradas na função `tela_questoes()`, caso a mensagem seja referente a pontuação final, o loop acabará.

Após o while, a última resposta do servidor com a pontuação do cliente é mostrada na função `tela_final()`.
```python
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))

    tela_Inicio()
    while True:
        question = s.recv(1024).decode()
        if question.__contains__('Sua pontuação'):
            break
        tela_questoes(question)

    tela_final(question)
```


Funcionamento do protocolo com explicação das mensagens trocadas

## Servidor

Para o envio de mensagens por parte do servidor, inicialmente foi definida uma lista de dicionários, que serão armazenadas em uma variável e aproveitada durante a troca de mensagens. A lista contém o enunciado e a resposta de cada pergunta.
```python
quiz_data = [
    {"pergunta": """1 - O que é um sistema distribuído aberto?
a) É um sistema que permite uma ampliação gradual de seus recursos
b) São sistemas de pequeno porte, alimentados por bateria
c) É um sistema que, por conter serviços e regras padronizadas, permite a comunicação entre aplicações de diferentes fornecedores
d) Nenhuma das opções
    """, "resposta_correta": "c)"},
    {"pergunta": """2 - O que se entende por escalabilidade de uma rede?
a) É o tempo decorrido após uma operação de envio ser executada
b) Capacidade de sua infraestrutura suportar o crescimento da rede
c) Capacidade da rede em garantir a correta entrega dos dados no destino
d) Capacidade de permitir que conversões ocorram somente se forem necessárias
    """, "resposta_correta": "b)"},
    {"pergunta": """3 - Qual o papel do middleware em um sistema distribuído?
a) Economia de recursos e compartilhamento de informações
b) Promover a comunicação entre os sistemas oferecendo a mesma interface para as aplicações
c) Para manter a independência entre os protocolos de cada camada
d) Prover um middleware padrão entre sistemas heterogêneos
    """, "resposta_correta": "b)"},
    {"pergunta": """4 - As linguagens XML e HTML possuem estrutura parecida, sendo essencialmente estruturada com a utilização de tags. O que os diferencia?
a) A XML especifica a estrutura dos dados, enquanto a HTML especifica o layout
b) A XML permite a criação de novas tags para uso pelas aplicações, enquanto HTML define um formato binário para representação de dados
c) A XML especiffica o layout, enquanto a HTML especifica a estrutura de dados
d) Nenhuma das opções
    """, "resposta_correta": "a)"},
    {"pergunta": """5 - O que é uma rede de sobreposição?
a) Rede formada por um conjunto de sensores que se comunicam para distribuição de informações
b) Rede onde os componentes trabalham um em prol do outro visando o cumprimento da tarefa
c) Rede responsável por manter a independência entre os protocolos de cada camada
d) Rede formada sobre outra rede, contendo apenas os nós e enlaces necessários ao funcionamento do sistema
    """, "resposta_correta": "d)"},
    {"pergunta": """6 - Qual a principal vantagem a ser obtida quando se monta um sistema distribuído para utilização emsubstituição a um sistema centralizado?
a) Somar o poder de processamento dos equipamentos na execução da tarefa.
b) Promover a comunicação entre os sistemas oferecendo a mesma interface para as aplicações.
c) Economia de recursos e compartilhamento de informações.
d) Garantir a integridade caso a aplicação não possa executar até o final.
    """, "resposta_correta": "a)"},
    {"pergunta": """7 - Em que a RMI é diferente da RPC?
a) RPC e RMI ocultam do programador aspectos importantes da distribuição, promovendo um elevado nível de transparência de acesso e de localização.
b) A RMI é voltada para invocação a métodos remotos (objetos) enquanto a RPC é baseada na comunicação entre processos por intermédio de chamadas de procedimentos.
c) A RMI é não voltada para invocação a métodos remotos (objetos) enquanto a RPC é baseada na interface de sistemas.
d) A RMI é voltada para banco de dados enquanto a RPC é baseada na comunicação entre processos por intermédio de chamadas de procedimentos.
    """,  "resposta_correta": "b)"},
    {"pergunta": """8 - Um dos objetivos de um sistema distribuído é permitir o acesso a recursos remotos. Por que isto é desejável?
a) Economia de recursos e coleta de informações.
b) Economia de recursos e restrições de informações.
c) Economia de recursos e compartilhamento de informações.
d) Disperdício de recursos e compartilhamento de informações.
    """,  "resposta_correta": "c)"},
    {"pergunta": """9 - O que é transparência de distribuição? Por que ela é desejada?
a) Capacidade de aparecer para o usuário como um sistema integrado. Quanto mais complexo for um sistema, maior será seu valor para aplicação.
b) Capacidade de aparecer para o usuário como um sistema de computação em nuvem. Quanto mais transparente for um sistema, mais fácil será de utilizá-lo.
c) Capacidade de se ocultar para o usuário como um sistema único. Quanto mais transparente for um sistema, maior será sua complexidade.
d) Capacidade de aparecer para o usuário como um sistema único. Quanto mais transparente for um sistema, mais fácil será de utilizá-lo.
    """,  "resposta_correta": "d)"},
    {"pergunta": """10 - Por que nem sempre é bom buscar a transparência total em um sistema distribuído?
a) Em determinadas situações (sistemas pervasivos, por exemplo) é melhor que o usuário saiba tratar-se de um sistema distribuído e conhecer suas limitações, sabendo assim o que esperar do sistema.
b) Usar a trasparência total pode tornar o sistema distribuído vulnerável.
c) Usar a trasparência total pode piorar a performance do sistema.
d) Usar a trasparência total pode aumentar o custo de desenvolvimento.
    """,  "resposta_correta": "a)"},
]
```
Para a dinâmica do jogo, foi feita uma função para obter a lista criada anteriormente e enviar de forma sequencial para o cliente, esperando a resposta para enviar cada pergunta.

Dentro da função, é iniciada a variável score que será responsável pela pontuação do cliente.

É feito um loop dentro da lista de perguntas e dentro dele, são realizadas as seguintes instruções:

Envio da pergunta para o cliente, usando a função sendall() para o envio e dentro dos parâmetros, é importante colocar a função encode() para enviar a pergunta (string) no formato de bytes. 

Na variável resposta recebe a resposta do cliente, é usada a função decode() para decodificar a mensagem recebida e armazenar em forma de string. 

É feita a verificação da resposta para poder incrementar a variável score em caso de pontuação.

Após o loop, é enviada a resposta final com a pontuação do cliente, após isso, a conexão acaba. 

def start_quiz(conn):
    score = 0
```python
    for question in quiz_data:
        conn.sendall(question['pergunta'].encode())
        resposta = conn.recv(1024).decode()

        if resposta.lower() == question["resposta_correta"].lower():
            score += 1
    if score < 5:
        emoji = '🥺'
    elif score <= 8:
        emoji = '🙂'
    else:
        emoji = '😁'

    conn.sendall(f"""OBRIGADO POR JOGAR!
Sua pontuação final é: {score}/{len(quiz_data)}
{emoji}""".encode())
```
## Cliente

Dentro do script referente ao cliente, foram feitas diversas funções para as situações propostas pelo servidor. Primeiramente, vale ressaltar que foi utilizada a biblioteca tkinter para mostrar as mensagens trocadas entre cliente e servidor.

### Tela de início

Função criada com o fito de “apresentar o jogo“ ao cliente. Ela não utiliza nenhuma mensagem recebida pelo servidor. 

Primeiramente, é iniciada a tela que será usada. 

São definidos: 

- O título da tela

- Os frames a serem utilizados

- O primeiro frame será responsável por colocar o texto de apresentação do jogo.

- O segundo frame terá um botão para iniciar o jogo.

No final é usada a função `mainloop()` para mostrar a tela.
```python
def tela_Inicio():
    root = tk.Tk()

    root.title('Quiz sistemas Distribuídos')
    frame1 = tk.Frame(root)
    frame2 = tk.Frame(root)

    titulo = tk.Label(frame1, text="Seja Bem-Vindo ao Quiz de Sistemas Distribuídos", justify=tk.CENTER, wraplength=500)
    titulo.config(font=("roboto-condensed", 25, ))
    titulo.pack(side=tk.LEFT)

    jogar = tk.Button(frame2, text='Jogar', command=root.destroy, width=50, justify=tk.LEFT, wraplength=350)
    jogar.config(font=("roboto-condensed", 12))
    jogar.pack()

    frame1.pack(padx=1, pady=1)
    frame2.pack(pady=10, padx=10)

    root.mainloop()
```

### Definição de respostas

Função criada para enumerar os tipos de respostas dentro do Quiz, utilizando a formatação de A,B,C e D.

- É utilizado a opção `"RETURN S.SENDALL"` para enviar as respostas escolhidas para o servidor em questão.

```python
def resposta1():
    resposta = 'a)'

    return s.sendall(resposta.encode())


def resposta2():
    resposta = 'b)'
    return s.sendall(resposta.encode())


def resposta3():
    resposta = 'c)'
    return s.sendall(resposta.encode())


def resposta4():
    resposta = 'd)'
    return s.sendall(resposta.encode())
```
### Tela de questões

![image](https://github.com/Marcos-Meireles/quiz-game/assets/82594356/45582ad1-77d4-4699-a3a9-7c69d78d9e04)

Função criado com o objetivo de “apresentar as questões” que serão discutidas dentro do Quiz.

São definidos:

- A pergunta que será respondida (em formatação “Título”).

- As opções (respostas) referente a pergunta retratada.

- Os frames a serem utilizados.

- Cada frame receberá cada alternativa enviada pelo servidor.

- A formatação visual da tela de perguntas e respostas.
```python
def tela_questoes(pergunta):

    respostas = pergunta.split('\n')
    questao = respostas[0]
    print(f"Pergunta: {questao}")
    root = tk.Tk()

    root.title('Quiz sistemas Distribuídos')
    frame1 = tk.Frame(root)
    frame2 = tk.Frame(root) 
    frame3 = tk.Frame(root)
    frame4 = tk.Frame(root)
    frame5 = tk.Frame(root)
    frame6 = tk.Frame(root)

    titulo = tk.Label(frame1,text=questao,justify=tk.CENTER, wraplength=500)
    titulo.config(font=("roboto-condensed", 16))
    titulo.pack(side=tk.LEFT)
```
### Tela de questões (código)

Modelo de codificação para a construção das opções de respostas para cada pergunta, de modo mais visual.

- É utilizado "tk.Button" para aplicar a cada modelo de resposta uma formatação de BOTÃO, para torná-lo executável.

- Frames utilizados para textualização das opções de respostas.

- Utiliza-se `"mainloop()"` para mostrar a tela com as alternativas referente a cada questão.
```python
    alternativa1 = tk.Button(frame2, text=respostas[1], command=resposta1, width=50, justify=tk.LEFT, wraplength=350,bd=3)
    alternativa1.config(font=("roboto-condensed", 12))
    alternativa1.pack()
    
    alternativa2 = tk.Button(frame3, text=respostas[2], command=resposta2, width=50, justify=tk.LEFT, wraplength=350,bd=3)
    alternativa2.config(font=("roboto-condensed", 12))
    alternativa2.pack()

    alternativa3 = tk.Button(frame4, text=respostas[3], command=resposta3, width=50, justify=tk.LEFT, wraplength=350,bd=3)
    alternativa3.config(font=("roboto-condensed", 12))
    alternativa3.pack()

    alternativa4 = tk.Button(frame5, text=respostas[4], command=resposta4, width=50, justify=tk.LEFT, wraplength=350,bd=3)
    alternativa4.config(font=("roboto-condensed", 12))
    alternativa4.pack()

    enviar = tk.Button(frame6, text='Enviar', command=root.destroy, width=30, justify=tk.LEFT,wraplength=350, bg='#a0a0a0',bd=3)
    enviar.config(font=("roboto-condensed", 12, 'bold'))
    enviar.pack()


    frame1.pack(padx=1, pady=1)
    frame2.pack(pady=10, padx=10)
    frame3.pack(padx=10, pady=10)
    frame4.pack(padx=10, pady=10)
    frame5.pack(padx=10, pady=10)
    frame6.pack(padx=10, pady=10)

    
    root.mainloop()
```

### Tela Final

Função para mostrar a tela final, responsável por demonstrar o resultado final do usuário, apresentando número de acertos referente as questões elaboradas dentro do jogo.

- O título da tela.

- Os frames que serão utilizados.

- Opção/Botão de saída.

- Utilização de `mainloop()` para ilustração da tela de resultados do Quiz.

```python
def tela_final(texto):
    root = tk.Tk()

    root.title('Quiz sistemas Distribuídos')
    frame1 = tk.Frame(root)
    frame2 = tk.Frame(root)
    frame3 = tk.Frame(root)

    titulo = tk.Label(frame1, text=texto, justify=tk.CENTER, wraplength=500)
    titulo.config(font=("roboto-condensed", 20))
    titulo.pack(side=tk.LEFT)

    sair = tk.Button(frame2, text='Sair', command=root.destroy, width=50, justify=tk.LEFT, wraplength=350)
    sair.config(font=("roboto-condensed", 12))
    sair.pack()

    consideracoes = tk.Label(frame3, text='Desenvolvido por: Antonio Cardoso, Enzo Bispo, Marcos Meireles, Samuel Vianna, Victor Glicério', justify=tk.LEFT)
    consideracoes.config(font=("roboto-condensed", 8))
    consideracoes.pack()

    frame1.pack(padx=1, pady=1)
    frame2.pack(pady=10, padx=10)
    frame3.pack(padx=30)

    root.mainloop()
```

# Execução

Como os dois scripts são feitos com a linguagem python, é preciso instalá-lo para executar os scripts.

Para a instalação basta realizar o download no site oficial da linguagem: https://www.python.org/.

Após a instalação, basta clicar com o botão direito no arquivo e selecionar 'Abrir com' e selecionar o python para executar. 

![image](https://github.com/Marcos-Meireles/quiz-game/assets/82594356/642544e2-80d0-4e7c-8c42-e05031fd958d)

Primeiramente, é executado o arquivo servidor.py para iniciar o servidor para começar a conexão e depois é executado o cliente.py.

- Início da execução do servidor:


![image](https://github.com/Marcos-Meireles/quiz-game/assets/82594356/3a05a811-426b-4397-a27c-1b06205c4031)


- Após a conexão com o cliente (executar o arquivo cliente.py):

![image](https://github.com/Marcos-Meireles/quiz-game/assets/82594356/1792e544-8b5d-41e4-b1ed-b4720ddc36b7)


- Tela de apresentação:

![image](https://github.com/Marcos-Meireles/quiz-game/assets/82594356/84d21deb-5ca1-4917-bad4-c89fce0e2260)


- Estrutura da pergunta (padrão utilizado durante o jogo):

![image](https://github.com/Marcos-Meireles/quiz-game/assets/82594356/a20d8f2f-c62d-4201-9db8-bae8998f2742)


- Tela final:

![image](https://github.com/Marcos-Meireles/quiz-game/assets/82594356/e559b9a6-9fc3-411e-81dd-acd773c50739)


# Localização dos códigos

Os códigos estão presentes para download no repositório do aluno Marcos Paulo Meireles na plataforma GitHub:

https://github.com/Marcos-Meireles/quiz-game
