from tkinter import *
from tkinter.ttk import *

janela = Tk()
janela.title("ComboBox")
janela.geometry('250x250')

combo = Combobox(janela)  # ⬇ Valores que irão aparecer no comboBox 
combo['values'] = ("Iguape", "Ilha Comprida","Registro","juquía","Miracatu","Cajati")
combo.current(1) #Define item selecionado (que sera mostrado no ComoboBox)
combo.pack()

janela.mainloop()
