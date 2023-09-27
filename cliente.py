import socket
import tkinter as tk

host = 'localhost'
port = 12345


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
def mostrar_questoes(pergunta):

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

    titulo = tk.Label(frame1,text=questao,justify=tk.CENTER, wraplength=500)
    titulo.config(font=("roboto-condensed", 20))
    titulo.pack(side=tk.LEFT)

    alternativa1 = tk.Button(frame2, text=respostas[1], command=resposta1, width=50, justify=tk.LEFT, wraplength=350)
    alternativa1.config(font=("roboto-condensed", 12))
    alternativa1.pack()
    
    alternativa2 = tk.Button(frame3, text=respostas[2], command=resposta2, width=50, justify=tk.LEFT, wraplength=350)
    alternativa2.config(font=("roboto-condensed", 12))
    alternativa2.pack()

    alternativa3 = tk.Button(frame4, text=respostas[3], command=resposta3, width=50, justify=tk.LEFT, wraplength=350)
    alternativa3.config(font=("roboto-condensed", 12))
    alternativa3.pack()

    alternativa4 = tk.Button(frame5, text=respostas[4], command=resposta4, width=50, justify=tk.LEFT, wraplength=350)
    alternativa4.config(font=("roboto-condensed", 12))
    alternativa4.pack()

    frame1.pack(padx=1, pady=1)
    frame2.pack(pady=10, padx=10)
    frame3.pack(padx=10, pady=10)
    frame4.pack(padx=10, pady=10)
    frame5.pack(padx=10, pady=10)
    
    root.mainloop()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    cont = 0
    while True:
        question = s.recv(1024).decode()
        mostrar_questoes(question)
        if not question:
            break

        print(f"Pergunta: {question}")

        # resposta = input('Sua resposta: ')
        # s.sendall(resposta.encode())
        cont+=1

    resultado = s.recv(1024).decode()
    print(resultado)
