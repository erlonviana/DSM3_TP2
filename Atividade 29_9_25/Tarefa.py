import os

from tkinter import * #importação da biblioteca
from tkinter import ttk, filedialog
from PIL import Image, ImageTk #biblioteca PIL possibilita o trabalho com imagens usando componente ImageTk
tela = Tk() ##nome da variavel para criação da tela

#titulo da barra de tarefas
tela.title("Trabalho Técnicas de Programação II") #define o titulo

#Configuração da cor da tela (opcional)
tela.configure(background='#88AED2') #define a cor de fundo

#Configuração do tamanho da tela
tela.geometry("700x700") #define o tamanho da tela

tela.resizable(True, True) #habilita reajuste da tela para altura e largura

#Tamanho máximo que a tela pode chegar
tela.maxsize(width=1000, height=700)

#Tamanho minimo que a tela pode chegar
tela.minsize(width=900, height=700)

# lbl_teste = Label(tela, text="Teste").place (x=10, y=10)
#lbl teste é o nome de identificação interno da label
#label é o tipo de componente
#tela a variavel que a label está ligado
#text="" é o texto a ser exibido na tela
#place o posicionamento da tela

#placeholder para os textos sumirem ao digitar:
def add_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.config(fg="gray")

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, "end")
            entry.config(fg="black")

    def on_focus_out(event):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.config(fg="gray")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

#Labels
lbl_titulo = Label (tela, text="Cadastro familiar", font=("Segoe UI", 20), fg="#1F1C19", bg=tela["bg"])
lbl_titulo.place (x=300, y=10)

lbl_nome = Label (tela, text="Nome", font=("Segoe UI", 12), fg="#1F1C19", bg=tela["bg"])
lbl_nome.place (x=10, y=60)

lbl_idade = Label (tela, text="Idade", font=("Segoe UI", 12), fg="#1F1C19", bg=tela["bg"])
lbl_idade.place (x=10, y=100)

lbl_telefone = Label (tela, text="Telefone", font=("Segoe UI", 12), fg="#1F1C19", bg=tela["bg"])
lbl_telefone.place (x=10, y=140)

lbl_parentesco = Label (tela, text="Grau de parentesco", font=("Segoe UI", 12), fg="#1F1C19", bg=tela["bg"])
lbl_parentesco.place (x=10, y=180)

lbl_endereco = Label (tela, text="Endereço", font=("Segoe UI", 12), fg="#1F1C19", bg=tela["bg"])
lbl_endereco.place (x=10, y=220)
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

#caixas de texto
txt_nome = Entry(tela, width=60, borderwidth=1, fg="blue", bg="white")
# txt_nome.pack() #usando place ao invés de pack
#txt_nome.insert(100, "Digite o seu nome")
txt_nome.place (x=70, y=65)
add_placeholder(txt_nome, "Digite seu nome")

txt_idade = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
# txt_idade.pack() #usando place ao invés de pack
# txt_idade.insert(0, "Digite sua idade")
txt_idade.place (x=70, y=105)
add_placeholder(txt_idade, "Digite sua idade")

txt_telefone = Entry(tela, width=20, borderwidth=1, fg="blue", bg="white")
# txt_telefone.pack()#usando place ao invés de pack
# txt_telefone.insert(0, "Digite seu telefone")
txt_telefone.place (x=90, y=145)
add_placeholder(txt_telefone, "Digite seu telefone")

#Lista suspensa
combo = ttk.Combobox(tela, width=18)
combo['values'] = ("Pai","Mãe","Filho/a","Irmã/irmão", "Avô/Avó","Tio/Tia")
combo.current(1) #define o item selecionado
# combo.pack() #usando place ao invés de pack

combo.place(x=160, y=185)


txt_endereco = Entry(tela, width=60, borderwidth=1, fg="blue", bg="white")
# txt_endereco.pack() #usando place ao invés de pack
# txt_endereco.insert(0, "Digite seu endereco")
txt_endereco.place (x=90, y=225)
add_placeholder(txt_endereco, "Digite seu endereço")

#definindo caminho das imagens
foto_salvar = PhotoImage(file = r"salvar.png")

#definindo caminho das imagens para os botões
foto_salvar = PhotoImage(file = r"icones/salvar.png")
foto_excluir = PhotoImage(file = r"icones/excluir.png")
foto_alterar = PhotoImage(file = r"icones/alterar.png")
foto_consultar = PhotoImage(file = r"icones/consultar.png")
foto_sair = PhotoImage(file = r"icones/sair.png")

#botões
btn_excluir = Button(tela, text="Excluir", image = foto_excluir, compound=TOP).place(x=200, y=310)
btn_alterar = Button(tela, text="Alterar", image=foto_alterar, compound=TOP).place(x=270, y=310)
btn_consultar = Button(tela, text="Consultar", image=foto_consultar, compound=TOP).place(x=340, y=310)
btn_sair = Button(tela, text="Sair", image=foto_sair, compound=RIGHT, command=tela.destroy).place(x=620, y=340)

#variável para armazenar a pasta padrão de localização da imagem
pasta_inicial = "" 

#Localização do arquivo e tipos de arquivos suportados
def escolher_imagem():
    caminho_imagem = filedialog.askopenfilename( #variável "caminho_imagem" só existe dentro dessa função "escolher_imagem"
        initialdir=pasta_inicial, 
        title="Escolha uma imagem",
        filetypes=(("Arquivos de imagem", "*.jpg;*.jpeg;*.png"),
                   ("Todos os arquivos", "*.*"))
    )
    
    #Abertura do arquivo atraves do PIL
    if caminho_imagem:
        imagem_pil = Image.open(caminho_imagem)
        largura, altura = imagem_pil.size

        if largura>150:
            proporcao = largura/150
            nova_altura = int(altura / proporcao)
            imagem_pil = imagem_pil.resize((110, nova_altura)) #redimensionamento de imagem

        imagem_tk = ImageTk.PhotoImage(imagem_pil)
        lbl_imagem = Label(tela, image=imagem_tk)
        lbl_imagem.image = imagem_tk
        lbl_imagem.place(x=600, y=50) #imagem escolhida será armazenada em uma Label(lbl_imagem)

#Botão chamando a função escolher imagem
btn_escolher = Button(tela, text="Escolher imagem", command=escolher_imagem) 
btn_escolher.place(x=605, y=230)

# === Tabela logo abaixo dos botões === CHAT CANTOU KKKKK
colunas = ("Nome", "Idade", "Telefone", "Parentesco", "Endereço", "Maior de idade?", "Pode votar?")
tabela = ttk.Treeview(tela, columns=colunas, show="headings", height=6)

# Cabeçalhos
for col in colunas:
    tabela.heading(col, text=col)
    tabela.column(col, width=120, anchor=CENTER)

# Posicionando a tabela abaixo dos botões
tabela.place(x=30, y=470)

# Inserindo 4 linhas
dados = [
    ("Érlon Viana dos Santos", 36, "99999-1111", "Filho", "Rua das Flores, 123", "Não", "Não"),
    ("Maria Sueli", 45, "98888-2222", "Mãe", "Av. Central, 456", "Sim", "Sim"),
    ("Joao Carlos", 55, "97777-3333", "Pai", "Rua dos Ipês, 789", "Sim", "Sim"),
    ("Everton Viana", 16, "96666-4444", "Filho", "Rua Azul, 321", "Não", "Não"),
]

for linha in dados:
    tabela.insert("", END, values=linha)

# Função para verificar maior de idade e se pode votar
def maior_idade(idade):
    try:
        idade = int(idade)
        if idade >= 18:
            return "Sim", "Sim"
        else:
            return "Não", "Não"
    except:
        return "Não informado", "Não informado"

# Função para salvar os dados na tabela
def salvar_dados():
    nome = txt_nome.get()
    idade = txt_idade.get()
    telefone = txt_telefone.get()
    parentesco = combo.get()
    endereco = txt_endereco.get()

    # Evitar placeholders como valores
    placeholders = ["Digite seu nome", "Digite sua idade", "Digite seu telefone", "Digite seu endereço"]
    if nome in placeholders or idade in placeholders or telefone in placeholders or endereco in placeholders:
        return  # não insere se algum campo está vazio ou com placeholder

    maior, pode_votar = maior_idade(idade)

    tabela.insert("", END, values=(nome, idade, telefone, parentesco, endereco, maior, pode_votar))

    # Limpar campos após salvar
    txt_nome.delete(0, END)
    txt_idade.delete(0, END)
    txt_telefone.delete(0, END)
    txt_endereco.delete(0, END)
    add_placeholder(txt_nome, "Digite seu nome")
    add_placeholder(txt_idade, "Digite sua idade")
    add_placeholder(txt_telefone, "Digite seu telefone")
    add_placeholder(txt_endereco, "Digite seu endereço")

#Botão salvar
btn_salvar = Button(tela, text="Salvar", image = foto_salvar, compound= TOP, command=salvar_dados).place(x=130, y=310)

#Fim do código
tela.mainloop()