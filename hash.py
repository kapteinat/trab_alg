import tkinter as tk

class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = [(key, value)]
        else:
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    break
            else:
                self.table[index].append((key, value))

    def get_sorted_table(self):
        sorted_table = []
        for bucket in self.table:
            if bucket is not None:
                sorted_table.extend(bucket)
        sorted_table.sort(key=lambda x: x[0])  # Ordena com base nas chaves
        return sorted_table

class HashTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabela Hash")
        self.root.geometry("800x600")
        
        self.hash_table = HashTable()
        
        self.label_name = tk.Label(root, text="Nome:")
        self.label_name.pack()
        
        self.entry_name = tk.Entry(root)
        self.entry_name.pack()
        
        self.label_key = tk.Label(root, text="Chave:")
        self.label_key.pack()
        
        self.entry_key = tk.Entry(root)
        self.entry_key.pack()
        
        self.add_button = tk.Button(root, text="Adicionar à Tabela Hash", command=self.add_to_hash)
        self.add_button.pack()
        
        self.display_button = tk.Button(root, text="Exibir Tabela", command=self.display_table)
        self.display_button.pack()
        
        self.text_output = tk.Text(root, height=10, width=50)
        self.text_output.pack()
        
    def add_to_hash(self):
        name = self.entry_name.get()
        key = self.entry_key.get()
        
        if name and key:
            self.hash_table.insert(key, name)
            self.text_output.delete(1.0, tk.END)  # Limpa o texto exibido
            self.text_output.insert(tk.END, f"Elemento adicionado: Chave: {key}, Nome: {name}\n")
        else:
            self.text_output.delete(1.0, tk.END)  # Limpa o texto exibido
            self.text_output.insert(tk.END, "Por favor, preencha ambos os campos.\n")

    def display_table(self):
        sorted_table = self.hash_table.get_sorted_table()
        table_str = "Tabela Hash (Ordenada por Chave):\n"
        for key, value in sorted_table:
            table_str += f"Chave: {key}, Nome: {value}\n"
        self.text_output.delete(1.0, tk.END)  # Limpa o texto exibido
        self.text_output.insert(tk.END, table_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = HashTableApp(root)
    root.mainloop()
