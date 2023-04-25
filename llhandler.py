from PBQPgraph import PBQPGraph

class LLHandler:

    def read_llvm_ir_file(file):
        # Abrir o arquivo IR do LLVM e ler todas as linhas
        lines = file.readlines()

        # Inicializar o dicionário que irá armazenar os arrays de strings de cada função
        functions = {}

        # Percorrer todas as linhas do arquivo
        for i in range(len(lines)):
            line = lines[i].strip()

            # Verificar se a linha indica o início de uma nova função
            if line.startswith('define'):
                # Obter o nome da função a partir da linha de código
                function_name = line.split()[2].split('(')[0]
                
                # Inicializar um novo array de strings para a função
                function_code = []

                # Adicionar cada linha de código subsequente da função até encontrar o final da função
                j = i
                while j < len(lines) and not lines[j].startswith('}'):
                    function_code.append(lines[j])
                    j += 1

                # Armazenar o array de strings da função no dicionário
                functions[function_name] = function_code

        # Retornar o dicionário contendo os arrays de strings de cada função
        return functions

    
    def analyze_registers(function_code):
        # Inicializar o dicionário de registradores vazio
        registers = {}

        # Percorrer todas as linhas de código da função
        for i in range(len(function_code)):
            line = function_code[i].strip()

            # Identificar os registradores utilizados na linha de código
            used_registers = set()
            for word in line.split():
                if word.startswith('%'):
                    if word[-1] in [',', ')', ']']:
                        word = word[:-1]
                    used_registers.add(word)

            # Atualizar as informações dos registradores utilizados na linha de código
            for register_name in used_registers:
                if register_name in registers:
                    # Atualizar a linha de última utilização e a quantidade de utilizações do registrador
                    registers[register_name][1] = i
                    registers[register_name][2] += 1
                else:
                    # Criar uma nova entrada para o registrador
                    registers[register_name] = [i, i, 1]
        return registers

    def create_graph(vRegisters, regCostArray):
        graph = PBQPGraph()
        for rName in vRegisters:
            node = vRegisters[rName]
            array = PBQPGraph.create_cost_array(regCostArray, node[2])
            graph.add_node(rName, array)
        for rName1 in vRegisters:
            for rName2 in vRegisters:
                if rName1 != rName2:
                    node1 = vRegisters[rName1]
                    node2 = vRegisters[rName2]
                    if node1[0] <= node2[0] <= node1[1] or node1[0] <= node2[1] <= node1[1] or node2[0] <= node1[0] <= node2[1] or node2[0] <= node1[1] <= node2[1]:
                        matrix = PBQPGraph.create_cost_matrix(graph.nodes[rName1], graph.nodes[rName2])
                        graph.add_edge(rName1, rName2, matrix)
        return graph
