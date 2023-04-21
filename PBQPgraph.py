from math import inf

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
    
    def create_basic_cost_array(regCost, spillCost):
        array = regCost
        array.append(spillCost)
        return array

    def create_basic_cost_matrix(array1, array2):
        n = len(array2)
        matrix = [array1] * n
        for i in range(n):
            for j in range(n):
                if i == j and i != n - 1:
                    matrix[i][j] = inf
                else:
                    matrix[i][j] += array2[j]
        return matrix
            
