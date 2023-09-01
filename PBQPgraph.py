import json

class PBQPGraph:
    def __init__(self):
        self.nodes = {}  # dicionário de nós (chave = ID do nó, valor = nó)
        self.edges = []  # lista de arestas
        
    def add_node(self, node_id, array, vType, uses, deepness):
        self.nodes[node_id] = {"array" : array, "type" : vType, "uses" : uses, "deepness" : deepness}
        
    def add_edge(self, node_id1, node_id2, matrix):
        for edge in self.edges:
            if (edge[0] == node_id1 and edge[1] == node_id2) or (edge[0] == node_id2 and edge[1] == node_id1):
                return
        self.edges.append((node_id1, node_id2, matrix))
    
    def create_cost_array(regCost, spillCost):
        array = regCost.copy()
        if spillCost is not None:
            array += spillCost
        return array

    def create_cost_matrix(array1, array2, spillCostLen):
        n = len(array2)
        matrix = []
        for i in range(n):
            aux = []
            for j in range(n):
                if i == j and i != n - spillCostLen:
                   aux.append("Infinity")
                else:
                    aux.append(array1[i] + array2[j])
            matrix.append(aux)
        return matrix
    
    def as_json(self, flagArray, flagMatrix, identLevel = 0):
        jsonString = ""
        jsonString += '\t' * identLevel + "{\n"
        jsonString += '\t' * (identLevel + 1) + "\"nodes\" : {\n"
        commaFlag = False 
        for node_name in self.nodes:
            if commaFlag:
                jsonString += ",\n"
            else:
                commaFlag = True
            jsonString += '\t' * (identLevel + 2) + "\"{}\" : {}\n".format(node_name,'{')
            jsonString += '\t' * (identLevel + 3) + "\"type\" : \"{}\",\n".format(self.nodes[node_name]["type"])
            jsonString += '\t' * (identLevel + 3) + "\"uses\" : {},".format(json.dumps(self.nodes[node_name]["uses"]))
            jsonString += '\t' * (identLevel + 3) + "\"deepness of uses\" : {}".format(json.dumps(self.nodes[node_name]["deepness"]))
            if flagArray:
                jsonString += ",\n" + '\t' * (identLevel + 3) + "\"cost array\" : {}\n".format(str(self.nodes[node_name]["array"]))
            else:
                jsonString += "\n"
            jsonString += '\t' * (identLevel + 2) + "}"
        jsonString += "\n" + '\t' * (identLevel + 1) + "},\n"

        jsonString += '\t' * (identLevel + 1) + "\"edges\" : [\n"
        commaFlag = False 
        for edge in self.edges:
            if commaFlag:
                jsonString += ",\n"
            else:
                commaFlag = True
            jsonString += '\t' * (identLevel + 2) + "{\n"
            jsonString += '\t' * (identLevel + 3) + "\"node 1\" : \"{}\",\n".format(edge[0])
            jsonString += '\t' * (identLevel + 3) + "\"node 2\" : \"{}\"\n".format(edge[1])

            if flagMatrix:
                jsonString += ",\n" + '\t' * (identLevel + 3) + "\"cost matrix\" : [\n"

                for arr in edge[2][:-1]:
                    jsonString +=  '\t' * (identLevel + 4) + json.dumps(arr) + ",\n"
                jsonString +=  '\t' * (identLevel + 4) + json.dumps(edge[2][-1]) + "\n"
                jsonString +=  '\t' * (identLevel + 3) + "]\n"

            else:
                jsonString += "\n"
            jsonString += '\t' * (identLevel + 2) + "}"
        jsonString += "\n" + '\t' * (identLevel + 1) + "]\n" 

        jsonString += '\t' * (identLevel) + "}"

        return jsonString            
