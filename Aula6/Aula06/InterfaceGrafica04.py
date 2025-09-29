#Para trabalharmos com imagen no Python 
# precisamos instalar uma biblioteca acesse o cmd ou terminal e digite pip install Pillow
from tkinter import filedialog

from tkinter import *
from tkinter.ttk import *

tela = Tk()
tela.title("ComboBox")
tela.geometry('250x250')

combo = Combobox(tela)  # ⬇ Valores que irão aparecer no comboBox 
combo['values'] = ("Iguape", "Ilha Comprida","Registro","juquía","Miracatu","Cajati")
combo.current(1) #Define item selecionado (que sera mostrado no ComoboBox)
combo.pack()

from PIL import Image, ImageTk #Biblioteca PIL possibilita o trabalho com image
#Para que seja possivel escolher uma imagem externa salvo no Computador é necessario o componente filedialog
pasta_inicial = "" #vamos criar uam variavel para armazenar a pasta padrão de localização da imagem,
# neste momento deixaremos em branco

#Localização do arquivo, e tipos de arquivos a ser utilizados
def escolher_imagem():
    caminho_imagem = filedialog.askopenfilename(initialdir=pasta_inicial,title="Escolha uma imagem",filetypes=(("Arquivo de imagem","*.jpg;*jpeg;*png"),("Todos os arquivos","*.*")))

#Abertura do arquivo atraves do PIL
    imagem_pil = Image.open(caminho_imagem)
    largura, altura = imagem_pil.size
    if largura > 150:
        proporcao = largura / 150
        nova_altura = int(altura/proporcao) #codigo com identação
        imagem_pil = imagem_pil.resize((110,nova_altura))#Redimensionamento da imagem
#Convertendo a imagem para formato compativel ao Tkinter
    imagem_tk = ImageTk.PhotoImage(imagem_pil)
    lbl_imagem = Label(tela,image=imagem_tk)
    lbl_imagem.image = imagem_tk
    lbl_imagem.place(x=10,y=50) #A imagem escolhida  será amazenada em uma Label(lbl_imagem)
#Botão chamando a função escolher
btn_escolher = Button(tela,text="Escolher imagem", command=escolher_imagem)
btn_escolher.place(x=10,y=140) #botã chamando a função escolher imagem

#define onde esta as imagens
foto_salvar = PhotoImage(file = r"icones\salvar.png")
foto_excluir = PhotoImage(file = r"icones\excuir.png")
foto_alterar = PhotoImage(file = r"icones\alterar.png")
foto_consultar = PhotoImage(file = r"icones\consultar.png")
foto_sair = PhotoImage(file = r"icones\sair.png")

#propriedade da imagem para localização da imagem
btn_salvar = Button(tela,text="Salvar",image=foto_salvar,compound=TOP).place(x=130,y=310)
btn_excluir = Button(tela,text="Excluir",image=foto_excluir,compound=TOP).place(x=200,y=310)
btn_alterar = Button(tela,text="Alterar",image=foto_alterar,compound=TOP).place(x=270,y=310)
btn_consultar = Button(tela,text="Consultar", image=foto_consultar,compound=TOP).place(x=340,y=310)
btc_sair = Button(tela,text="Sair",image=foto_sair,compound=RIGHT).place(x=620,y=340)

tela.mainloop()
