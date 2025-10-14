from tkinter import *
tela = Tk()

tela.title("Radio Buttons")
#Cor da tela
tela.configure(background='#1e3743')
#Configurar tamanho da tela
tela.geometry("700x600")

var = StringVar() #Define o tipo de variavel
var.set("m") #Define qual RadioButton estará selecionado na tela iniciar
                                         #⬇Define o tipo de variavel que irá guardar as opções do RadioButton
rdb_buttonm = Radiobutton(tela,text="M",variable=var,value="m").place(x=20,y=40) #
rdb_buttonf = Radiobutton(tela,text="F",variable=var,value="f").place(x=20,y=60)

tela.mainloop()