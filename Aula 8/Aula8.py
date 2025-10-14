from tkinter import *
from tkinter import messagebox
import subprocess

tela = Tk()
tela.title("Acesso ao Sistema")
tela.geometry("400x200")
tela.resizable(False, False)
largura = 400
altura = 200

#Criação de funções: tela de login

def sair():
    resposta = messagebox.askquestion("Sair do sistema ?", "Você tem certeza que deseja sair?")
    if resposta == 'yes':
        tela.destroy()

def validar_acesso(usuario, senha):
    
    if usuario == 'admin' and senha == '123':
        abrir_app()

    else:
        messagebox.showerror("Erro de login", "Usuario ou senha incorretos")

def abrir_app():
    tela.destroy()
    subprocess.run(["python", "exemplo_mongo.py"])

def click_botao():
    usuario = txt_usuario.get()
    senha = txt_senha.get()
    validar_acesso(usuario, senha) #função validar acesso será chamada no botão, passando como parametros usuario e senha

    lbl_usuario = Label(tela, text="Usuario").place(x=50, y=60)
    lbl_senha = Label(tela, text="Senha").place(x=50, y=100)
    #campos txt não podem ter .place no final pois podem armazenar os valores x e y ao invés das
    #entradas do usuario
    txt_senha = Entry(tela, width=20, show="*")
    txt_senha.place(x=100, y=100)
    txt_usuario = Entry(tela, width=20)
    txt_usuario.place(x=100, y=60)

    foto_acesso = PhotoImage(file=r"icones\acesso.png")
    foto_sair = PhotoImage(file =r"icones\sair.png")

    btn_usuario = Button(tela, text="Acessar", image=foto_acesso, compound=TOP, command=click_botao)
    btn_usuario.place(x=250, y=50)

    btn_sair = Button(tela, text="Sair", image=foto_sair, compound=TOP, command=sair)
    btn_sair.place(x=320, y=50)

    larugura_screen = tela.winfo_screenwidth()
    altura_screen = tela.winfo_screenheight()
    posx = larugura_screen / 2 - largura / 2
    posy = altura_screen / 2 - altura / 2
    tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
    tela.mainloop()





