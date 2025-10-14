from tkinter import filedialog #escolha de imagens
from PIL import Image, ImageTk #bibliote PIL possibilita o trabalho com imagens usando componente ImageTk

pasta_inicial = "" #variável para armazenar a pasta padrão de localização da imagem

#inicio da função

#Localização do arquivo e tipos de arquivos suportados
def escolher_imagem():
    caminho_imagem = filedialog.askopenfilename(initialdir=pasta_inicial, title="Escolha uma imagem",
                                                filetypes=(("Arquivos de imagem", "*.jpg;*.jpeg;*.png"),
                                                  ("Todos os arquivos", "*.*")))
    

