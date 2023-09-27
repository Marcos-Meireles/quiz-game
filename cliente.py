import socket
import tkinter as tk

host = 'localhost'
port = 12345

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


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))

    tela_Inicio()
    while True:
        question = s.recv(1024).decode()
        if question.__contains__('Sua pontuação'):
            break
        tela_questoes(question)

        # resposta = input('Sua resposta: ')
        # s.sendall(resposta.encode())



        # resposta = input('Sua resposta: ')
        # s.sendall(resposta.encode())


    tela_final(question)
