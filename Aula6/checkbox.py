from tkinter import *

tela = Tk()
tela.title("Open file")
tela.geometry("300x300")

def show():
    Label(tela, text = var.get()).pack()

var = StringVar() #tipo de variável armazenada
# var = IntVar()

chk_button = Checkbutton(tela, text="Check box", variable = var, onvalue="On", offvalue="Off")
chk_button.deselect()
chk_button.pack()

Button(tela, text="Show me", command=show).pack() #.pack() é um método do tkinter que organiza os widgets

tela.mainloop()