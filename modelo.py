from controle import *

class Elemento:
    def __init__(self, nome, chave):
        self.nome = nome
        self.chave = chave


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