from view import *
from modelo import *


class Controller:
    def __init__(self, root):
        self.view = View(root, self.on_button_click)

    def on_button_click(self):
        elementos = []
        input_text = self.view.entry.get("1.0", tk.END)
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
            self.view.output.delete("1.0", tk.END)
            self.view.output.insert(tk.END, output_text)
