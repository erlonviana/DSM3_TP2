from tkinter import *
tela = Tk()
tela.title("open file")
tela.geometry("300x300")

def show():
    Label(tela,text=var.get()).pack()
var = StringVar() #Define tipo de variavel que irá guardar as opções do RadioButon
#var = IntVar()
                                                               #⬇ onvalue/offvalues = valor quando check estiver selecionado ou não
chk_button = Checkbutton(tela,text="check box", variable=var,onvalue="on",offvalue="off")
chk_button.deselect()
chk_button.pack()

Button(tela,text="show me", command=show).pack()

tela.mainloop()