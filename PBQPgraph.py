import numpy as np

class PBQPGraph:
    def __init__(self):
        self.nodes = {}  # dicionário de nós (chave = ID do nó, valor = nó)
        self.edges = []  # lista de arestas
        
    def add_node(self, node_id, array):
        self.nodes[node_id] = array
        
    def add_edge(self, node_id1, node_id2, matrix):
        self.edges.append((node_id1, node_id2, matrix))

    def as_dict(self):
        data = {
            "nodes": self.nodes,
            "edges": self.edges
        }
        return data
    
    def create_cost_array(regCost, spillCost):
        array = regCost.copy()
        array.append(spillCost)
        return array

    def create_cost_matrix(array1, array2):
        n = len(array2)
        matrix = []
        for i in range(n):
            aux = []
            for j in range(n):
                if i == j and i != n - 1:
                   aux.append("Infinity")
                else:
                    aux.append(array1[i] + array2[j])
            matrix.append(aux)
        return matrix
            
