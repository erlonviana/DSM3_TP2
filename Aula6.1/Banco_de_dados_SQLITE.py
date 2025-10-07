import sqlite3  # importando SQlite
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import datetime
import os

# Conecta ao banco
conn = sqlite3.connect("MyDB.db") # nome do banco de dados
cur = conn.cursor() #mensageiro entre o programa e o banco de dados

# Mostra o caminho completo do arquivo
print(f"✅ Banco de dados criado em: {os.path.abspath('MyDB.db')}")

tela = Tk()
tela.title("Controle de pessoas")
tela.geometry("800x600")
var = StringVar() #variavel especial para botões de radio ("quadro negro vazio")
var.set("m") #Escreve "m" na variável ("quadro negro")("masculino")

# Criar tabela
cur.execute("CREATE TABLE IF NOT EXISTS pessoas(codigo INT primary key, nome TEXT, idade INT, sexo TEXT, altura REAL, peso REAL," \
            "cidade TEXT, datanasc TEXT, dataAtual TEXT, dataCadastro TEXT, descricao TEXT)")

conn.commit() # o comando que confirma e salva permanentemente as alterações no banco de dados.
conn.close()

# Função para obter data atual
def get_data_atual():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# CRIANDO BANCO DE DADOS SQLITE - INSERÇÃO
def inserção():
    try:
        conn = sqlite3.connect("MyDB.db")
        cur = conn.cursor()

        cur.execute('INSERT INTO pessoas VALUES (:codigo, :nome, :idade, :sexo, :altura, :peso, :cidade, :datanasc, :dataatual, :dataCadastro, :descricao)', 
                    {'codigo': txt_codigo.get(), 
                     'nome': txt_nome.get(), 
                     'idade': txt_idade.get(), 
                     'sexo': var.get(), 
                     'altura': txt_altura.get(), 
                     'peso': txt_peso.get(), 
                     'cidade': cmb_cidade.get(),
                     'datanasc': txt_data_nascimento.get(), 
                     'dataatual': get_data_atual(),
                     'dataCadastro': get_data_atual(), 
                     'descricao': txt_descricao.get("1.0", END)})
        
        conn.commit()
        conn.close()
        
        limpar_campos()
        messagebox.showinfo("Sucesso", "Registro inserido com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao inserir: {str(e)}")

# FUNÇÃO CONSULTA
def consulta():
    conn = sqlite3.connect("MyDB.db")
    cur = conn.cursor()
    cur.execute('SELECT *, oid FROM pessoas')
    records = cur.fetchall()

    # Limpa área de resultados
    for widget in frame_resultados.winfo_children():
        widget.destroy()

    # Cabeçalho
    Label(frame_resultados, text="CÓDIGO", font=("Arial", 10, "bold"), bg="lightgray", width=10).grid(row=0, column=0, padx=1, pady=1)
    Label(frame_resultados, text="NOME", font=("Arial", 10, "bold"), bg="lightgray", width=20).grid(row=0, column=1, padx=1, pady=1)
    Label(frame_resultados, text="IDADE", font=("Arial", 10, "bold"), bg="lightgray", width=10).grid(row=0, column=2, padx=1, pady=1)
    Label(frame_resultados, text="SEXO", font=("Arial", 10, "bold"), bg="lightgray", width=10).grid(row=0, column=3, padx=1, pady=1)
    Label(frame_resultados, text="AÇÕES", font=("Arial", 10, "bold"), bg="lightgray", width=20).grid(row=0, column=4, padx=1, pady=1)

    # Dados
    for i, rec in enumerate(records, 1):
        Label(frame_resultados, text=str(rec[0]), bg="white", width=10).grid(row=i, column=0, padx=1, pady=1)
        Label(frame_resultados, text=str(rec[1]), bg="white", width=20).grid(row=i, column=1, padx=1, pady=1)
        Label(frame_resultados, text=str(rec[2]), bg="white", width=10).grid(row=i, column=2, padx=1, pady=1)
        Label(frame_resultados, text=str(rec[3]), bg="white", width=10).grid(row=i, column=3, padx=1, pady=1)
        
        # Botões de ação
        frame_botoes = Frame(frame_resultados, bg="white")
        frame_botoes.grid(row=i, column=4, padx=1, pady=1)
        
        Button(frame_botoes, text="Editar", command=lambda r=rec: carregar_dados(r), 
               bg="blue", fg="white", font=("Arial", 8)).pack(side=LEFT, padx=2)
        Button(frame_botoes, text="Excluir", command=lambda r=rec[0]: excluir_registro(r), 
               bg="red", fg="white", font=("Arial", 8)).pack(side=LEFT, padx=2)

    conn.close()

# FUNÇÃO EXCLUIR
def excluir_registro(codigo):
    if messagebox.askyesno("Confirmar", "Deseja realmente excluir este registro?"):
        conn = sqlite3.connect("MyDB.db")
        cur = conn.cursor()
        cur.execute('DELETE FROM pessoas WHERE codigo = ?', (codigo,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sucesso", "Registro excluído com sucesso!")
        consulta()

# FUNÇÃO CARREGAR DADOS PARA EDIÇÃO
def carregar_dados(registro):
    txt_codigo.delete(0, END)
    txt_codigo.insert(0, registro[0])
    txt_nome.delete(0, END)
    txt_nome.insert(0, registro[1])
    txt_idade.delete(0, END)
    txt_idade.insert(0, registro[2])
    var.set(registro[3])
    txt_altura.delete(0, END)
    txt_altura.insert(0, registro[4])
    txt_peso.delete(0, END)
    txt_peso.insert(0, registro[5])
    cmb_cidade.set(registro[6])
    txt_data_nascimento.delete(0, END)
    txt_data_nascimento.insert(0, registro[7])
    txt_descricao.delete("1.0", END)
    txt_descricao.insert("1.0", registro[10])

# FUNÇÃO UPDATE
def update():
    try:
        conn = sqlite3.connect("MyDB.db")
        cur = conn.cursor()
        
        cur.execute("""UPDATE pessoas SET 
                    nome = :nome,
                    idade = :idade,
                    sexo = :sexo,
                    altura = :altura,
                    peso = :peso,
                    cidade = :cidade,
                    datanasc = :datanasc,
                    dataAtual = :dataAtual,
                    descricao = :descricao
                    WHERE codigo = :codigo""",
                    {'nome': txt_nome.get(),
                     'idade': txt_idade.get(),
                     'sexo': var.get(),
                     'altura': txt_altura.get(),
                     'peso': txt_peso.get(),
                     'cidade': cmb_cidade.get(),
                     'datanasc': txt_data_nascimento.get(),
                     'dataAtual': get_data_atual(),
                     'descricao': txt_descricao.get("1.0", END),
                     "codigo": txt_codigo.get()})
        
        conn.commit()
        conn.close()
        
        limpar_campos()
        consulta()
        messagebox.showinfo("Sucesso", "Registro atualizado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao atualizar: {str(e)}")

# FUNÇÃO LIMPAR CAMPOS
def limpar_campos():
    txt_codigo.delete(0, END)
    txt_nome.delete(0, END)
    txt_idade.delete(0, END)
    var.set("m")
    txt_altura.delete(0, END)
    txt_peso.delete(0, END)
    cmb_cidade.set("")
    txt_data_nascimento.delete(0, END)
    txt_descricao.delete("1.0", END)

# WIDGETS DA INTERFACE
frame_cadastro = LabelFrame(tela, text="Cadastro de Pessoas", font=("Arial", 12, "bold"), padx=10, pady=10)
frame_cadastro.pack(padx=10, pady=5, fill="x")

# Linha 1
Label(frame_cadastro, text="Código:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=2)
txt_codigo = Entry(frame_cadastro, width=10, font=("Arial", 10))
txt_codigo.grid(row=0, column=1, pady=2, padx=5)

Label(frame_cadastro, text="Nome:*", font=("Arial", 10)).grid(row=0, column=2, sticky="w", pady=2)
txt_nome = Entry(frame_cadastro, width=30, font=("Arial", 10))
txt_nome.grid(row=0, column=3, pady=2, padx=5)

Label(frame_cadastro, text="Idade:", font=("Arial", 10)).grid(row=0, column=4, sticky="w", pady=2)
txt_idade = Entry(frame_cadastro, width=10, font=("Arial", 10))
txt_idade.grid(row=0, column=5, pady=2, padx=5)

# Linha 2
Label(frame_cadastro, text="Sexo:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=2)
frame_sexo = Frame(frame_cadastro)
frame_sexo.grid(row=1, column=1, pady=2, padx=5, sticky="w")
Radiobutton(frame_sexo, text="Masculino", variable=var, value="m", font=("Arial", 9)).pack(side=LEFT)
Radiobutton(frame_sexo, text="Feminino", variable=var, value="f", font=("Arial", 9)).pack(side=LEFT)

Label(frame_cadastro, text="Altura (m):", font=("Arial", 10)).grid(row=1, column=2, sticky="w", pady=2)
txt_altura = Entry(frame_cadastro, width=10, font=("Arial", 10))
txt_altura.grid(row=1, column=3, pady=2, padx=5)

Label(frame_cadastro, text="Peso (kg):", font=("Arial", 10)).grid(row=1, column=4, sticky="w", pady=2)
txt_peso = Entry(frame_cadastro, width=10, font=("Arial", 10))
txt_peso.grid(row=1, column=5, pady=2, padx=5)

# Linha 3
Label(frame_cadastro, text="Cidade:", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=2)
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Brasília", "Salvador", "Fortaleza", "Recife", "Porto Alegre", "Curitiba", "Manaus"]
cmb_cidade = ttk.Combobox(frame_cadastro, values=cidades, width=20, font=("Arial", 10))
cmb_cidade.grid(row=2, column=1, pady=2, padx=5, columnspan=2)

Label(frame_cadastro, text="Data Nasc.:", font=("Arial", 10)).grid(row=2, column=3, sticky="w", pady=2)
txt_data_nascimento = Entry(frame_cadastro, width=15, font=("Arial", 10))
txt_data_nascimento.grid(row=2, column=4, pady=2, padx=5)
Label(frame_cadastro, text="(dd/mm/aaaa)", font=("Arial", 8), fg="gray").grid(row=2, column=5, sticky="w", pady=2)

# Linha 4
Label(frame_cadastro, text="Descrição:", font=("Arial", 10)).grid(row=3, column=0, sticky="nw", pady=2)
txt_descricao = Text(frame_cadastro, width=50, height=3, font=("Arial", 10))
txt_descricao.grid(row=3, column=1, pady=2, padx=5, columnspan=5, sticky="we")

# Frame dos Botões
frame_botoes = Frame(frame_cadastro)
frame_botoes.grid(row=4, column=0, columnspan=6, pady=10)

Button(frame_botoes, text="Inserir", command=inserção, bg="green", fg="white", 
       font=("Arial", 10, "bold"), width=10).pack(side=LEFT, padx=5)
Button(frame_botoes, text="Atualizar", command=update, bg="blue", fg="white", 
       font=("Arial", 10, "bold"), width=10).pack(side=LEFT, padx=5)
Button(frame_botoes, text="Consultar", command=consulta, bg="orange", fg="white", 
       font=("Arial", 10, "bold"), width=10).pack(side=LEFT, padx=5)
Button(frame_botoes, text="Limpar", command=limpar_campos, bg="gray", fg="white", 
       font=("Arial", 10, "bold"), width=10).pack(side=LEFT, padx=5)

# Frame de Resultados
frame_resultados_container = LabelFrame(tela, text="Registros Cadastrados", font=("Arial", 12, "bold"), padx=10, pady=10)
frame_resultados_container.pack(padx=10, pady=5, fill="both", expand=True)

# Canvas e Scrollbar para resultados
canvas = Canvas(frame_resultados_container) #O Canvas no Tkinter é como uma "tela em branco" ou "área de desenho" onde você pode colocar widgets e criar interfaces mais complexas
scrollbar = ttk.Scrollbar(frame_resultados_container, orient="vertical", command=canvas.yview)
frame_resultados = Frame(canvas)

frame_resultados.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

canvas.create_window((0, 0), window=frame_resultados, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Consulta inicial
consulta()

tela.mainloop()