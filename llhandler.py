from PBQPgraph import PBQPGraph

class LLHandler:

    types = {
        "i1" : "i8",
        "i8" : "i8",
        "i16" : "i16",
        "i32" : "i32",
        "i64" : "i64",
        "float" : "float",
        "double" : "double",
        "i1*" : "ptr",
        "i8*" : "ptr",
        "i16*" : "ptr",
        "i32*" : "ptr",
        "i64*" : "ptr",
        "float*" : "float*",
        "double*" : "double*",
        "icmp" : "i8",
        "inbounds" : "ptr",
        "alloca" : "ptr",
        "label" : "label"
    }

    regStarts = ["%0", "%1", "%2", "%3", "%4", "%5", "%6", "%7", "%8", "%9", "%."]

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
        profundidade = 0

        # Percorrer todas as linhas de código da função
        for i in range(len(function_code)):
            line = function_code[i].strip()

            loopLabels = []
            # Identificar os registradores utilizados na linha de código
            used_registers = []
            rType = {"%0" : "label"}
            flagLoop = False
            flagType = True
            words = line.split()
            
            if len(words) > 0: 
                if words[0].endswith(":"):
                    rType["%" + words[0][:-1]] = "label"
                    if words[0] in loopLabels:
                        profundidade -= 1
                elif words[0].startswith('%.0'):
                    profundidade += 1
                    flagLoop = True
                for word in words:
                    if any([word.startswith(x) for x in LLHandler.regStarts]):
                        if word[-1] in [',', ')', ']']:
                            word = word[:-1]
                        used_registers.append(word)
                    elif flagType and word in LLHandler.types and len(used_registers) > 0:
                        rType[used_registers[0]] = LLHandler.types[word]
                        flagType = False
                if flagLoop:
                    loopLabels.append(used_registers[-1][1:])

            # Atualizar as informações dos registradores utilizados na linha de código
            for register in used_registers:
                if register in registers:
                    # Atualizar a linha de última utilização e a quantidade de utilizações do registrador
                    registers[register][1] = i
                    registers[register][3].append(profundidade)
                else:
                    # Criar uma nova entrada para o registrador
                    registers[register] = [i, i, "", [profundidade]]
            
            for register_name in rType:
                try:
                    registers[register_name][2] = rType[register_name]
                except:
                    continue

        return registers

    def create_graph(vRegisters, regCostArray, costFunc):
        graph = PBQPGraph()
        for rName in vRegisters:
            node = vRegisters[rName]
            if costFunc is None:
                aux = None
                spillCostLen = 0
            else:
                aux = costFunc(node[2], node[3])
                spillCostLen = len(aux)
            array = PBQPGraph.create_cost_array(regCostArray, aux)
            graph.add_node(rName, array, node[2], node[3])
        for rName1 in vRegisters:
            for rName2 in vRegisters:
                if rName1 != rName2:
                    node1 = vRegisters[rName1]
                    node2 = vRegisters[rName2]
                    if node1[0] <= node2[0] < node1[1] or node1[0] <= node2[1] <= node1[1] or node2[0] <= node1[0] < node2[1] or node2[0] <= node1[1] <= node2[1]:
                        matrix = PBQPGraph.create_cost_matrix(graph.nodes[rName1]["array"], graph.nodes[rName2]["array"], spillCostLen)
                        graph.add_edge(rName1, rName2, matrix)
        return graph
