import tkinter as tk
from tkinter import messagebox
from controle import *

class View:
    def __init__(self, root, on_button_click, on_button_click1):
        self.root = root
        self.root.title("Aplicação com Menu")
        self.root.geometry("800x600")

        # Crie um frame para as páginas
        self.page_frame = tk.Frame(self.root)
        self.page_frame.pack(fill=tk.BOTH, expand=True)

        # Crie um dicionário para mapear as páginas aos seus nomes
        self.pages = {}

        # Crie as páginas e adicione ao dicionário
        self.pages["Ordenacao"] = self.criar_pagina_ordenacao()
        self.pages["Hash"] = self.criar_pagina_hash()
        self.pages["Grafos"] = self.criar_pagina_grafo()

        # Exiba a página de ordenação por padrão
        self.mostrar_pagina("Ordenacao")

        # Crie a barra de menus
        self.configurar_menu()

    def criar_pagina_ordenacao(self):
        pagina = tk.Frame(self.page_frame)
        pagina.configure(bg="white")
        
        # Conteúdo da página de ordenação
        label1 = tk.Label(pagina, text="Insira os elementos (nome, chave) separados por vírgula:")
        label1.pack()

        entry = tk.Text(pagina, height=10, width=40)
        entry.pack()

        # Crie um frame para os botões
        button_frame = tk.Frame(pagina)
        button_frame.pack()

        button = tk.Button(button_frame, text="Ordenar Merge", command=self.on_button_click)
        button.pack(side=tk.LEFT)

        button1 = tk.Button(button_frame, text="Ordenar Quick", command=self.on_button_click1)
        button1.pack(side=tk.LEFT)

        output = tk.Text(pagina, height=10, width=40)
        output.pack()

        return pagina

    def criar_pagina_hash(self):
        pagina = tk.Frame(self.page_frame)
        pagina.configure(bg="white")
        
        # Conteúdo da página de tabela hash
        label = tk.Label(pagina, text="Página de Tabela Hash")
        label.pack()
        # Adicione outros widgets da página de tabela hash

        return pagina
    
    def criar_pagina_grafo(self):
        pagina = tk.Frame(self.page_frame)
        pagina.configure(bg="white")
        
        # Conteúdo da página de tabela hash
        label = tk.Label(pagina, text="Página de Tabela grafo")
        label.pack()
        # Adicione outros widgets da página de tabela hash

        return pagina

    def mostrar_pagina(self, nome_pagina):
        # Oculta todas as páginas
        for nome, pagina in self.pages.items():
            pagina.pack_forget()
        
        # Exibe a página especificada
        self.pages[nome_pagina].pack(fill=tk.BOTH, expand=True)

    def configurar_menu(self):
        barra_de_menus = tk.Menu(self.root)

        # Crie um submenu "Páginas"
        menu_paginas = tk.Menu(barra_de_menus, tearoff=0)
        for nome in self.pages:
            menu_paginas.add_command(label=nome, command=lambda n=nome: self.mostrar_pagina(n))

        # Adicione o submenu "Páginas" à barra de menus
        barra_de_menus.add_cascade(label="Páginas", menu=menu_paginas)

        self.root.config(menu=barra_de_menus)
