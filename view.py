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
    abrir_janela(2)

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
