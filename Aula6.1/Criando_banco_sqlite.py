import sqlite3
from tkinter import ttk
from tkinter import messagebox, Tk, Label, Entry, Button, StringVar, END
from PIL import Image, ImageTk

tela = Tk()
tela.title("Controle de pessoas")
var = StringVar()
var.set("m")
largura = 800
altura = 600

#Cria database
conn = sqlite3.connect("MyDb.db")

#Criar cursor
cursor = conn.cursor()

#Criar tabela
conn.execute('CREATE TABLE IF NOT EXISTS pessoas(codigo INT primary key, nome TEXT, idade INT,' \
'sexo  TEXT, altura REAL, peso REAL, cidade TEXT, dataNasct TEXT, dataAtual TEXT, dataCadastro TEXT,' \
'descricao TEXT)')

#Insere dados na tabela
cursor.execute('INSERT INTO pessoas VALUES (:codigo, :nome, :idade, :sexo, :altura, :peso, :cidade, :datanasc,' \
':dataAtual, :dataCadastro, :descricao)',
{
    'codigo': txt_codigo.get(),
    'nome': txt_nome.get(),
    'idade': txt_idade.get(),
    'sexo': var.get(),
    'altura': txt_altura.get(),
    'peso': txt_peso.get(),
    'cidade': cmb_cidade.get(),
    'datanasc': txt_data_nascimento.get(),
    'dataAtual': txt_data_atualizacao.get(),
    'dataCadastro': txt_data_cadastro.get(),
    'descricao': txt_descricao.get()
})

#faz consulta na tabela
cursor.execute('SELECT *, oid FROM pessoas')

records = cursor.fetchall()

#mostra resultados encontrados
print_records = ""
for rec in records:
    print_records += 'Codigo: ' + str(rec[0]) + ' Nome: ' + str(rec[1]) + '\nIdade: ' + str(rec[2]) + \
                     ' Sexo: ' + str(rec[3]) + '\nAltura: ' + str(rec[4]) + ' Peso: ' + str(rec[5]) + '\n\n'

#create and positioning Label for the result (label e posição de exibição dos dados)
Label(tela, text=print_records).place(x=20, y=320)

#Deleta registro
cur.execute('DELETE FROM pessoas WHERE oid=' + txt_codigo.get())



#Commit changes
conn.commit()

#Close Connection 
conn.close()
messagebox.

#Clear text boxes (limpar caixas de texto)
txt_nome.delete(0, END)
txt_idade.delete(0, END)
txt_altura.delete(0, END)
txt_descricao.delete(0, END)

