import socket
import tkinter as tk

host = 'localhost'
port = 12345


def escolha(resposta):
    return s.sendall(resposta.encode())

def mostrar_questoes(pergunta):

    respostas = pergunta.split('\n')
    questao = respostas[0]

    root = tk.Tk()
    root.title('Quiz sistemas Distribuídos')
    frame1 = tk.Frame(root)
    frame2 = tk.Frame(root)
    frame3 = tk.Frame(root)
    frame4 = tk.Frame(root)
    frame5 = tk.Frame(root)
    frame6 = tk.Frame(root)

    titulo = tk.Label(frame1, text=questao, justify=tk.CENTER, wraplength=500)
    titulo.config(font=("roboto-condensed", 20))
    titulo.pack(side=tk.LEFT)

    alternativa1 = tk.Button(frame2, text=respostas[1], command=escolha('a)'), width=50, justify=tk.LEFT, wraplength=350)
    titulo.config(font=("roboto-condensed", 12))
    alternativa1.pack()

    alternativa2 = tk.Button(frame3, text=respostas[2], command=escolha('b)'), width=50, justify=tk.LEFT, wraplength=350)
    titulo.config(font=("roboto-condensed", 12))
    alternativa2.pack()

    alternativa3 = tk.Button(frame4, text=respostas[3], command=escolha('c)'), width=50, justify=tk.LEFT, wraplength=350)
    titulo.config(font=("roboto-condensed", 12))
    alternativa3.pack()

    alternativa4 = tk.Button(frame5, text=respostas[4], command=escolha('d)'), width=50, justify=tk.LEFT, wraplength=350)
    titulo.config(font=("roboto-condensed", 12))
    alternativa4.pack()

    enviar = tk.Button(frame6,text='Enviar',command=root.destroy, width=50, justify=tk.LEFT, wraplength=350)
    titulo.config(font=("roboto-condensed", 20))
    enviar.pack()

    frame1.pack(padx=1, pady=1)
    frame2.pack(pady=10, padx=10)
    frame3.pack(padx=10, pady=10)
    frame4.pack(padx=10, pady=10)
    frame5.pack(padx=10, pady=10)
    frame6.pack(padx=10, pady=10)


    root.mainloop()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    cont = 0
    while cont < 10:
        question = s.recv(1024).decode()
        mostrar_questoes(question)
        if not question:
            break
        # resposta = input('Sua resposta: ')
        # s.sendall(resposta.encode())
        cont += 1


resultado = s.recv(1024).decode()
print(resultado)
