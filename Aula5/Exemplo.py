from tkinter import * #importação da biblioteca
tela = Tk() ##nome da variavel para criação da tela

#titulo da barra de tarefas
tela.title("Fatec Registro") #define o titulo

#Configuração da cor da tela (opcional)
tela.configure(background='#1e3743') #define a cor de fundo

#Configuração do tamanho da tela
tela.geometry("700x600") #define o tamanho da tela

tela.resizable(True, True) #habilita reajuste da tela para altura e largura

#Tamanho máximo que a tela pode chegar
tela.maxsize(width=800, height=700)

#Tamanho minimo que a tela pode chegar
tela.minsize(width=500, height=300)

# lbl_teste = Label(tela, text="Teste").place (x=10, y=10)
#lbl teste é o nome de identificação interno da label
#label é o tipo de componente
#tela a variavel que a label está ligado
#text="" é o texto a ser exibido na tela
#place o posicionamento da tela

lbl_nome = Label (tela, text="Nome", font="Arial 20 bold italic", fg="#FF8C00").place (x=10, y=10)
lbl_cpf = Label(tela, text="CPF", font="Times 15 italic", fg="#7CFC00").place (x=10, y=50)
#font=fonte, fg = cor da fonte e bg=cor do fundo

#dimensões da tela
largura = 800
altura = 300

#resolução do sistema (tela)
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenheight()

#define posição da tela centralizada
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

#visualização do tamanho da tela no terminal
print(largura_screen, altura_screen)

#definição do geometry
tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

#caixa de texto
txt_nome = Entry(tela, width=20, borderwidth=5, fg="blue", bg="white")
txt_nome.pack()
txt_nome.insert(0, "Digite o seu nome")

#criando função no python
def meu_click():
    lbl_hello = Label(tela, text="Bem-vindo" + txt_nome.get())
    lbl_hello.pack()

#criando botão
btn_botao = Button(tela, text="Click", command=meu_click) #cria o botão e o texto; command chama a função
btn_botao.pack() #pack, faz com que o widget esteja juntamente com o widget pai (neste caso é a tela)



tela.mainloop()