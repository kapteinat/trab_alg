import tkinter as tk
from modelo import *
from controle import *
from tkinter import messagebox

# Função para criar e exibir uma nova janela
def abrir_janela(numero_janela):
    nova_janela = tk.Toplevel(janela)
    nova_janela.title(f"Janela {numero_janela}")
    nova_janela.geometry("800x600")
    label = tk.Label(nova_janela, text=f"Esta é a janela {numero_janela}")
    label.pack()

# Função para criar uma nova janela quando o primeiro botão é pressionado
def abrir_ordena():
    nova_janela = tk.Toplevel(janela)
    nova_janela.title("Ordenacao")
    nova_janela.geometry("800x600")
    label = tk.Label(nova_janela, text="Insira os elementos (nome, chave) separados por vírgula:")
    label.pack()

    entry = tk.Text(nova_janela, height=10, width=40)
    entry.pack()

    button_frame = tk.Frame(nova_janela)
    button_frame.pack()

    def on_button_click1():
        elementos = []
        input_text = entry.get("1.0", tk.END)
        lines = input_text.split('\n')

        for line in lines:
            parts = line.strip().split(',')
            if len(parts) == 2:
                nome, chave = parts
                try:
                    chave = int(chave)
                    elemento = Elemento(nome, chave)
                    elementos.append(elemento)
                except ValueError:
                    messagebox.showerror("Erro", "A chave deve ser um número inteiro.")

        if elementos:
            sorted_elementos = merge_sort(elementos)
            output_text = "\n".join([f"Nome: {elemento.nome}, Chave: {elemento.chave}" for elemento in sorted_elementos])
            output.delete("1.0", tk.END)
            output.insert(tk.END, output_text)

    def on_button_click():
        elementos = []
        input_text = entry.get("1.0", tk.END)
        lines = input_text.split('\n')

        for line in lines:
            parts = line.strip().split(',')
            if len(parts) == 2:
                nome, chave = parts
                try:
                    chave = int(chave)
                    elemento = Elemento(nome, chave)
                    elementos.append(elemento)
                except ValueError:
                    messagebox.showerror("Erro", "A chave deve ser um número inteiro.")

        if elementos:
            sorted_elementos = quick_sort(elementos, compare_func=lambda x, y: x.chave <= y.chave)
            output_text = "\n".join([f"Nome: {elemento.nome}, Chave: {elemento.chave}" for elemento in sorted_elementos])
            output.delete("1.0", tk.END)
            output.insert(tk.END, output_text)
        

    button = tk.Button(button_frame, text="Ordenar Merge", command=on_button_click)
    button.pack(side=tk.LEFT)

    button1 = tk.Button(button_frame, text="Ordenar Quick", command=on_button_click1)
    button1.pack(side=tk.LEFT)

    output = tk.Text(nova_janela, height=10, width=40)
    output.pack()


# Função para criar uma nova janela quando o segundo botão é pressionado
def abrir_hash():
    def add_to_hash():
        name = entry_name.get()
        key = entry_key.get()
        
        if name and key:
            hash_table.insert(key, name)
            text_output.delete(1.0, tk.END)  # Limpa o texto exibido
            text_output.insert(tk.END, f"Elemento adicionado: Chave: {key}, Nome: {name}\n")
        else:
            text_output.delete(1.0, tk.END)  # Limpa o texto exibido
            text_output.insert(tk.END, "Por favor, preencha ambos os campos.\n")

    def display_table():
        sorted_table = hash_table.get_sorted_table()
        table_str = "Tabela Hash (Ordenada por Chave):\n"
        for key, value in sorted_table:
            table_str += f"Chave: {key}, Nome: {value}\n"
        text_output.delete(1.0, tk.END)  # Limpa o texto exibido
        text_output.insert(tk.END, table_str)
    
    
    janela_hash = tk.Toplevel(janela)
    janela_hash.title("Hash")
    janela_hash.geometry("800x600")
        
    hash_table = HashTable()
    
    label_name = tk.Label(janela_hash, text="Nome:")
    label_name.pack()
    
    entry_name = tk.Entry(janela_hash)
    entry_name.pack()
    
    label_key = tk.Label(janela_hash, text="Chave:")
    label_key.pack()
    
    entry_key = tk.Entry(janela_hash)
    entry_key.pack()
    
    add_button = tk.Button(janela_hash, text="Adicionar à Tabela Hash", command=add_to_hash)
    add_button.pack()
    
    display_button = tk.Button(janela_hash, text="Exibir Tabela", command=display_table)
    display_button.pack()
    
    text_output = tk.Text(janela_hash, height=10, width=50)
    text_output.pack()


    


# Função para criar uma nova janela quando o terceiro botão é pressionado
def abrir_janela3():
    abrir_janela(3)

janela = tk.Tk()
janela.title("Janela Principal")
janela.geometry("400x300")

# Cria os botões
botao1 = tk.Button(janela, text="Ordenação", command=abrir_ordena)
botao2 = tk.Button(janela, text="Hash", command=abrir_hash)
botao3 = tk.Button(janela, text="Grafo", command=abrir_janela3)

# Exibe os botões na janela principal
botao1.pack()
botao2.pack()
botao3.pack()

janela.mainloop()
