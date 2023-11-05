import tkinter as tk
from tkinter import messagebox
#teste
class View:
    def __init__(self, root, on_button_click, on_button_click1):
        self.root = root
        self.root.title("Ordenação de Vetor")
        self.root.geometry("800x600")
        self.root.configure(bg="purple")

        self.label1 = tk.Label(self.root, text="Insira os elementos (nome, chave) separados por vírgula:")
        self.label1.pack()

        self.entry = tk.Text(self.root, height=10, width=40)
        self.entry.pack()

        # Crie um frame para os botões
        button_frame = tk.Frame(self.root)
        button_frame.pack()

        self.button = tk.Button(button_frame, text="Ordenar Merge", command=on_button_click)
        self.button.pack(side=tk.LEFT)

        self.button1 = tk.Button(button_frame, text="Ordenar Quick", command=on_button_click1)
        self.button1.pack(side=tk.LEFT)

        self.output = tk.Text(self.root, height=10, width=40)
        self.output.pack()
