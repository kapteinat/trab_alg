import tkinter as tk
from tkinter import messagebox

class View:
    def __init__(self, root, on_button_click):
        self.root = root
        self.root.title("Ordenação de Vetor")
        self.root.geometry("800x600")
        self.root.configure(bg="purple")

        self.label1 = tk.Label(self.root, text="Insira os elementos (nome, chave) separados por vírgula:")
        self.label1.pack()

        self.entry = tk.Text(self.root, height=10, width=40)
        self.entry.pack()

        self.button = tk.Button(self.root, text="Ordenar", command=on_button_click)
        self.button.pack()

        self.output = tk.Text(self.root, height=10, width=40)
        self.output.pack()
