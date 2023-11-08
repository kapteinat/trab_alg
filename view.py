import tkinter as tk
from modelo import *
from controle import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx

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
def abrir_grafo():
    # Dicionário para armazenar os nomes dos nós
    node_names = {}

    # Função para criar um grafo com base nos dados fornecidos
    def create_graph():
        key = key_entry.get()
        name = name_entry.get()
        
        G.add_node(key, name=name)
        
        # Salvar o nome do nó no dicionário
        node_names[key] = name
        
        # Atualiza o canvas
        update_graph_canvas(G)

    # Função para adicionar uma aresta entre nós
    def add_edge():
        node1 = node1_entry.get()
        node2 = node2_entry.get()
        
        if not G.has_node(node1) or not G.has_node(node2):
            messagebox.showerror("Erro", "Um ou ambos os nós não existem no grafo.")
            return
        
        G.add_edge(node1, node2)
        
        # Atualiza o canvas
        update_graph_canvas(G)

    # Função para realizar a busca em largura no grafo
    def breadth_first_search():
        start_node = start_node_entry.get()
        
        if not G.has_node(start_node):
            messagebox.showerror("Erro", f"O nó '{start_node}' não existe no grafo.")
            return
        
        bfs_tree = nx.bfs_tree(G, source=start_node)
        
        # Atualiza o canvas
        update_graph_canvas(bfs_tree, labels=node_names)

    # Função para realizar a busca em profundidade no grafo
    def depth_first_search():
        start_node = start_node_entry.get()
        
        if not G.has_node(start_node):
            messagebox.showerror("Erro", f"O nó '{start_node}' não existe no grafo.")
            return
        
        dfs_tree = nx.dfs_tree(G, source=start_node)
        
        # Atualiza o canvas
        update_graph_canvas(dfs_tree, labels=node_names)

    # Função para atualizar o canvas com o novo grafo
    def update_graph_canvas(graph, labels=None):
        plt.clf()
        pos = nx.spring_layout(graph)
        
        if labels is None:
            labels = {}
            for node in graph.nodes:
                labels[node] = node + " (" + node_names.get(node, "") + ")"
        
        nx.draw(graph, pos, with_labels=True, labels=labels)
        canvas.draw()
    
     
    
    
    janela_hash = tk.Toplevel(janela)
    janela_hash.title("Busca em Largura e Profundidade em grafos")
    janela_hash.geometry("800x600")
    
    # Criação do grafo vazio
    G = nx.Graph()

    # Cria a entrada para a chave
    key_label = tk.Label(janela_hash, text="Chave:")
    key_label.pack()
    key_entry = tk.Entry(janela_hash)
    key_entry.pack()

    # Cria a entrada para o nome
    name_label = tk.Label(janela_hash, text="Nome:")
    name_label.pack()
    name_entry = tk.Entry(janela_hash)
    name_entry.pack()

    # Botão para criar o grafo
    create_button = tk.Button(janela_hash, text="Criar Nó no Grafo", command=create_graph)
    create_button.pack()

    # Criação de um novo frame para as operações de busca
    search_frame = tk.Frame(janela_hash)
    search_frame.pack()

    # Cria a entrada para o nó de início
    start_node_label = tk.Label(search_frame, text="Nó de Início (Chave):")
    start_node_label.pack(side=tk.LEFT)
    start_node_entry = tk.Entry(search_frame)
    start_node_entry.pack(side=tk.LEFT)

    # Botão para busca em largura
    bfs_button = tk.Button(search_frame, text="Buscar em Largura", command=breadth_first_search)
    bfs_button.pack(side=tk.LEFT)

    # Botão para busca em profundidade
    dfs_button = tk.Button(search_frame, text="Buscar em Profundidade", command=depth_first_search)
    dfs_button.pack(side=tk.LEFT)

    # Adicionar nós e arestas
    edge_frame = tk.Frame(janela_hash)
    edge_frame.pack()

    node1_label = tk.Label(edge_frame, text="Nó 1 (Chave):")
    node1_label.pack(side=tk.LEFT)
    node1_entry = tk.Entry(edge_frame)
    node1_entry.pack(side=tk.LEFT)

    node2_label = tk.Label(edge_frame, text="Nó 2 (Chave):")
    node2_label.pack(side=tk.LEFT)
    node2_entry = tk.Entry(edge_frame)
    node2_entry.pack(side=tk.LEFT)

    edge_button = tk.Button(edge_frame, text="Conectar Nós", command=add_edge)
    edge_button.pack(side=tk.LEFT)

    # Cria o canvas para exibir o grafo
    figure = plt.figure(figsize=(6, 6))
    canvas = FigureCanvasTkAgg(figure, master=janela_hash)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()
    

janela = tk.Tk()
janela.title("Janela Principal")
janela.geometry("400x300")

# Cria os botões
botao1 = tk.Button(janela, text="Ordenação", command=abrir_ordena)
botao2 = tk.Button(janela, text="Hash", command=abrir_hash)
botao3 = tk.Button(janela, text="Grafo", command=abrir_grafo)

# Exibe os botões na janela principal
botao1.pack()
botao2.pack()
botao3.pack()

janela.mainloop()
